import multiprocessing as mp
import time

def start_process(instance_state, event):
    instance_state['instance01'] = [True,'localhost:50051',30]
    instance_state['instance02'] = [True,'localhost:50052',30]
    instance_state['instance03'] = [True,'localhost:50053',30]
    instance_state['instance02'] = [True,'localhost:50054',30]
    instance_state['instance02'] = [True,'localhost:50055',30]
    time.sleep(5)
    event.set()