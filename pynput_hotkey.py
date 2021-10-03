from pynput import keyboard

def MainFunction():
    print('Global hotkey activated!')

def DetectKey(f):
    return lambda k: f(l.canonical(k))

AssignedKey = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+<alt>+h'), MainFunction)

with keyboard.Listener(
        on_press=DetectKey(AssignedKey.press),
        on_release=DetectKey(AssignedKey.release)) as l:
    l.join()