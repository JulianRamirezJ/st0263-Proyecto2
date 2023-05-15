import multiprocessing as mp
from Monitor_S import monitor_s


def main():
    with mp.Manager() as manager:
        instance_state = manager.dict()
        monitor_p = mp.Process(target=monitor_s.start_process, args=(instance_state,))
        monitor_p.start()
        monitor_p.join()


if __name__ == '__main__':
    main()