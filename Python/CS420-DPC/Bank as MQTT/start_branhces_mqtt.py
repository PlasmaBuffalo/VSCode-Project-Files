from subprocess import Popen, PIPE
from multiprocessing import Process

if __name__ == "__main__":

    processes = []
    for i in range(5):
        proc = Popen(['python3', 'branch_mqtt.py', str(i)],
                     stderr=PIPE, stdout=PIPE)
        processes.append(proc)

    for proc in processes:
        stderr, stdout = proc.communicate()
        print(stderr, stdout)
