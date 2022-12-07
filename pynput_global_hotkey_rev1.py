# This script is not working on HP laptop

from pynput.keyboard import Key, GlobalHotKeys

print('\nWorking \nPress F12 to exit')

# Pass DAS script hotkey into main function
def transfer_function1():
    print("F1 pressed")

def transfer_function2():
    print("F2 pressed")

def exit_function():
    exit()

# Assign Python hotkeys to DAS script hotkeys
HOTKEY1 = '<F1>'
HOTKEY2 = '<F2>'
HOTKEY12 = '<F12>'

DASHOTKEY1 = Key.f1
DASHOTKEY2 = Key.f2
DASHOTKEY12 = Key.f12

with GlobalHotKeys({
        HOTKEY1 : transfer_function1,
        HOTKEY2 : transfer_function2,
        HOTKEY12 : exit_function}) as MappedResult:
    MappedResult.join()