import time

lastTime = time.time()

while True:
    timeDelta = time.time() - lastTime
    if timeDelta > 1:
        lastTime = time.time()
        print('')