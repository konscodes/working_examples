from pynput.mouse import Listener
import logging
import time

clicktime = 0
releasetime = 0
difference = 0

def DoubleClick(x, y, button, pressed):
    global releasetime
    global clicktime
    global difference

    if pressed:
        clicktime = time.time()
        difference = clicktime - releasetime
        print(difference)
        if difference < 0.25:
            PrintMessage()
    else:
        releasetime = time.time()
    
    return clicktime, releasetime

def PrintMessage():
    print("Doubleclick")

with Listener(on_click=DoubleClick) as listener:
    listener.join()