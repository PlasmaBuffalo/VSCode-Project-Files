# - Take the file I provided and add an additional thread that takes a users input and calculates the factorial of the number provided.
# -The user input should be in the form of an integer.
# -Once you receive the integer, calculate the factorial.
# -Print the answer to the console.
# -You can wrap this functionality in a forever loop ("while True: take input"), or try to match the style of the PrintTime thread.
# -Expected Output: No matter how long the user waits to input a number, the timestamp should continuously print to the console.

from cgi import print_arguments
from threading import Thread, Lock
from datetime import datetime
import numpy as np

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


# *********
# cntrl+c will stop command line program
class Factorial(Thread):
    def __init__(self): super().__init__()

    def run(self):

        while True:  # while finding output

            val = input("Enter your value: ")

            outcome = np.math.factorial(int(val))  # type: ignore

            print("outcome: " + str(outcome))

# ***********
# class description : prints the time for each second that passes


class PrintTime(Thread):

    def __init__(self, is_running):
        super().__init__()
        self._isRunning = is_running
        self._lastTime = datetime.now()

    def run(self):

        while self._isRunning:
            # print time every 1 second
            # .timestamp() gives us seconds
            timeDelta = datetime.now().timestamp() - self._lastTime.timestamp()
            if timeDelta > 1:
                self._lastTime = datetime.now()
                print('')
                print(str(self._lastTime))


class IsRunning(object):

    def __init__(self):
        self._isRunning = True

    def isRunning(self):
        return self._isRunning

    def setIsRunning(self, is_running):
        self._isRunning = is_running


if __name__ == "__main__":

    isRunning = IsRunning()

    printTime = PrintTime(isRunning)
    printTime.start()

# *************
    factorial = Factorial()
    factorial.start()

# *************
