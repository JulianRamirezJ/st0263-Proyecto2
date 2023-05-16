import multiprocessing as mp
from Monitor_S import monitor_s
from Controller import controller


def main():
    with mp.Manager() as manager:
        instance_state = manager.dict()
        event = mp.Event()
        controller_asg = mp.Process(target=controller.start_process, args=(instance_state, event))
        monitor = mp.Process(target=monitor_s.start_process, args=(instance_state, event))
        controller_asg.start()
        monitor.start()
        controller_asg.join()
        monitor.join()


if __name__ == '__main__':
    main()