'''python hotkey script to call 2 different functions 
with key values as arguments when F1 or F2 are pressed'''

import keyboard

def func1(key):
    print("F1 is pressed with value: ", key)

def func2(key):
    print("F2 is pressed with value: ", key)

# define hotkeys
keyboard.add_hotkey('F1', lambda: func1("value1"))
keyboard.add_hotkey('F2', lambda: func2("value2"))

# run the program until 'F12' is pressed
keyboard.wait('F12')