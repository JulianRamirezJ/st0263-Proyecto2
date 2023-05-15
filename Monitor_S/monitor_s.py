import multiprocessing as mp
import random as rm
import time as t

def start_process(instance_state, event):
    event.wait()
    print("M_S started")
    instance_state['instance01'] = [True,30]
    instance_state['instance02'] = [True,40]
    while True:
        r = rm.randint(0, 100)
        if  r <= 10:
            for key in instance_state.keys():
                instance_state[key] = [False, 0]
        elif r <= 30:
            for key in instance_state.keys():
                instance_state[key] = [True, 15]
        elif r <= 60:
            for key in instance_state.keys():
                instance_state[key] = [True, 60]
        print(instance_state)
        t.sleep(3)