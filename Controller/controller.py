import multiprocessing as mp
import time

def start_process(instance_state, event):
    time.sleep(5)
    event.set()