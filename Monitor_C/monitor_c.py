import grpc
from concurrent import futures

from service_pb2_grpc import MonitorServicer, add_MonitorServicer_to_server
from service_pb2 import Alive, Metric

#Redefine methods or actions that we want the server to do when receibing an order
class MonitorService(MonitorServicer):
    #request is the param we definedd in proto

    #This method test if server is alive
    def is_alive(self, request, context):
        return Alive(alive = "Holi")
    
    #Register order takes order and response with OrderConfirmation
    def get_metric(self, request, context):
        return Metric(delivery = 5)
    

def start():
    #Inside this method we will start to generate our service

    #How many threads or concurrent services to execute at the same time
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    #Add service to server
    add_MonitorServicer_to_server(MonitorService(), server)
    
    #Where to listen
    server.add_insecure_port('[::]:50051')
    print("server running in port 50051")

    #Start server
    server.start()

    #Terminal where server is executed stays alive to see current state of server
    server.wait_for_termination()


if __name__ == "__main__":
    start()