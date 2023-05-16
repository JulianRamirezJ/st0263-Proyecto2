import grpc
from concurrent import futures
import threading
import random


from service_pb2_grpc import MonitorServicer, add_MonitorServicer_to_server
from service_pb2 import Alive, Metric

cpu_usage = random.choice([10,15,20])
delay = 10
current_delay = 0
up = True

def change_cpu():
    global cpu_usage
    global delay
    global current_delay
    global up
    threading.Timer(2.0, change_cpu).start()
    print(cpu_usage)
    if current_delay > 0:
        current_delay += 1
        if(current_delay == delay):
            current_delay = 0
    else:
        if up:
            cpu_usage += 5
        else:
            cpu_usage -= 5
        if cpu_usage == 95:
            up = False
            current_delay += 1
        elif cpu_usage == 20:
            up = True
            current_delay += 1


#Redefine methods or actions that we want the server to do when receibing an order
class MonitorService(MonitorServicer):
    global cpu_usage
    #request is the param we definedd in proto

    #This method test if server is alive
    def is_alive(self, request, context):
        return Alive(alive = "True")
    
    #Register order takes order and response with OrderConfirmation
    def get_metric(self, request, context):
        return Metric(delivery = cpu_usage)
    

def start():
    change_cpu()
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
