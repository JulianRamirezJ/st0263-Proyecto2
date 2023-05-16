import multiprocessing as mp
import random as rm
import time as t
import grpc
from Monitor_S import service_pb2
from Monitor_S import service_pb2_grpc

def start_process(instance_state, event):
    event.wait()
    print("M_S started")
    PORT = ""
    while True:
        process_instances(instance_state,'50051')
        print(instance_state)
        t.sleep(3)


def process_instances(instance_state, PORT):
    for key in instance_state.keys():
        current_instance = instance_state[key]
        instance_address = current_instance[1]+':'+PORT
        try:
            channel = grpc.insecure_channel(instance_address)
            stub = service_pb2_grpc.MonitorStub(channel)
            alive = get_alive(stub)
            metric = 0
            if alive == "True":
                metric = get_metric(stub)
            instance_state[key] = [alive, current_instance[1], metric]
        except:
            instance_state[key] = [False, current_instance[1], 0]


def get_alive(stub):
    response = stub.is_alive(service_pb2.Nulo())
    return response.alive


def get_metric(stub):
    response = stub.get_metric(service_pb2.Nulo())
    return response.delivery