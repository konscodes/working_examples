from pynput import keyboard

def MainFunction():
    print("Executing MainFunction \n")

def ExitFunction():
    print("Executing ExitFunction \n")
    quit()

UserHotkey = "<ctrl>+<alt>+h"
SystemHotkey = "<ctrl>+<alt>+i"

with keyboard.GlobalHotKeys({
        UserHotkey : MainFunction,
        SystemHotkey : ExitFunction}) as MappedResult:
    MappedResult.join()