from threading import Thread, Lock
import numpy
from datetime import datetime 

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

            
class PrintTime(Thread):

    def __init__(self, is_running):
        super().__init__()
        self._isRunning = is_running
        self._lastTime  = datetime.now()
        
    def run(self):
    
        while self._isRunning.isRunning():
            # print time every 1 second
            timeDelta = datetime.now().timestamp() - self._lastTime.timestamp() # .timestamp() gives us seconds
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
