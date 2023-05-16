import multiprocessing as mp
import time

def start_process(instance_state, event):
    instance_state['instance01'] = [True,'localhost',30]
    instance_state['instance02'] = [True,'localhost',30]
    instance_state['instance03'] = [True,'localhost',30]
    instance_state['instance02'] = [True,'localhost',30]
    instance_state['instance02'] = [True,'localhost',30]
    time.sleep(5)
    event.set()