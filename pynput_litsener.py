from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse    import Listener as MouseListener
from pynput.keyboard import Key
from pywinauto import keyboard as PywinautoKeyboard
import logging

logging.basicConfig(filename=("log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def end_rec(key):
    logging.info(str(key))

def on_press(key):
    logging.info(str(key))

def on_move(x, y):
    logging.info("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        # Press and release space
        #keyboard.press(Key.ctrl)
        #keyboard.press('c')
        #keyboard.release(Key.ctrl)
        #keyboard.release('c')
        PywinautoKeyboard.send_keys('^c')

with MouseListener(on_click=on_click) as listener:
    with KeyboardListener(on_press=on_press) as listener:
        listener.join()