#import the required modules
import keyboard 

#define the functions to be called
def F1():
    print("F1 pressed")

def F2():
    print("F2 pressed")

#wait for the keys to be pressed
keyboard.add_hotkey('F1', F1) 
keyboard.add_hotkey('F2', F2) 

#run the program until 'esc' is pressed
keyboard.wait('esc')