'''
GUI automation script to suplement DAS hotkey

Idea: calculate stop distance based on current position size and set dollar risk

DAS hotkey script (Long): 
CXL ALLSYMB;SwitchTWnd;Route=Stop;Share=Pos;StopPrice=50/Pos;StopPrice=AvgCost-StopPrice;StopType=MARKET;TIF=DAY;SELL=Send;

Problem: DAS scripting language doesnt support Risk/Position opperation; moreover DAS API is 100$ per month
Solution: read montage controls with python library for GUI automation pywinauto; perform calculation in python; return desired value;

Notes: 
- script will put the new stop distance in Price field and hit the hotkey to send the order
- if there are many montage windows in use all of them should be in popout mode (right click the header --> pop out)
- two hotkeys are defined within a script; one for activating the python part; another for passing into DAS

Requirements:
- Pythin 3.8.0
- Pywinauto 0.6.8
- Pynput 1.6.7

Preparation:
1. Set first key combination in python to start the script
2. Add the below hotkey to DAS (Long)
CXL ALLSYMB;SwitchTWnd;Route=Stop;StopPrice=AvgCost-Price;StopType=MARKET;TIF=DAY;SELL=Send;
3. Set second key combination in python to pass into your DAS
4. Set your dollar risk in python script
5. Run the script

How to use:
1. Make sure that montage window is active
2. Hit the hotkey defined in Preparation Step1
3. Profit ;) the correct order should be placed

Change log:
v0.6 
- Added position direction detection
- Added DAS hotkeys for long and short

v0.5
- Added hotkey module to run the script
- Added error handling

v0.4
- Basic functionality reached

''' 

from pywinauto import Application                       # for window detection and connection
from pywinauto import keyboard as PywinautoKeyboard     # for sending key commands into DAS
from pynput import keyboard as PynputKeyboard           # for hotkeys to start and stop the script
from pywinauto.findwindows import ElementNotFoundError  # for error handling
from pywinauto.base_wrapper import ElementNotEnabled    # for error handling
import time                                             # for debug

def MainFunction():
    try:
        print("\nExecuting MainFunction \n")

        # Connect to active app
        app = Application(backend="win32").connect(active_only="True")

        # Select active window
        MontageWindow = app.window(active_only="True")
        MontageWindow.draw_outline()

        # Define controls (Need P button, Shares field, Price field)
        PositionButton = MontageWindow.P
        PositionButton.draw_outline()   # Draws an outline for fields used by the script
        Price = MontageWindow.PEdit
        Price.draw_outline()
        Shares = MontageWindow.Edit2
        Shares.draw_outline()
        Route = MontageWindow.ComboBox4
        Route.draw_outline()
        
        # Define get function
        def GetMontageVariables():
            global CurrentPrice
            global PositionSize
            global TradeDirection
            CurrentPrice = Price.get_line(0)
            PositionButton.click()
            PositionDirectional = Shares.get_line(0)
            if  "-" in PositionDirectional:
                TradeDirection = "Short"
                PositionSize = PositionDirectional.replace("-", "")
            else:
                TradeDirection = "Long"  
            print(" CurrentPrice: ", CurrentPrice)
            print(" CurrentPosition: ", PositionSize)
            return PositionSize

        # Get current variables
        print("\nOriginal: ")
        GetMontageVariables()

        # Perform calculations
        StopDistance = round((SetRisk/int(PositionSize)), 2)
        print("\n Calculated StopDistance: ", StopDistance)

        # Replace variables
        Route.select(0)                     # Set LIMIT route to make sure Price field is enabled 
        Price.set_edit_text(StopDistance)   # Set variable value
        print("\nAfter change: ")
        GetMontageVariables()

        # Send DAS hotkey
        if TradeDirection == "Short":
            PywinautoKeyboard.send_keys(DasHotkeyShort)
            print("\nDetected Short position. Sending ", DasHotkeyShort, " hotkey to DAS")
        else:    
            PywinautoKeyboard.send_keys(DasHotkeyLong)
            print("\nDetected Long position. Sending ", DasHotkeyLong, " hotkey to DAS")
        PrintMessage()

    except ElementNotFoundError:
        print("\nError: active element not found. Make sure DAS trader montage window is selected")
        PrintMessage()
    except ElementNotEnabled:
        print("\nError: active element is not enabled. Make sure Price field is enabled")
        PrintMessage()
    except Exception as error:
        print("\nUnexpected error... ", str(error))
        PrintMessage()

def ExitFunction():
    print("\nExecuting ExitFunction \n")
    quit()

def PrintMessage():
    print("\nPress ", StartHotkey, " to run the script or ", SystemHotkey, " to exit.")

# Define user variables
StartHotkey = "<Ctrl>+<Alt>+<Home>"     # User hotkey to run the script (free text format)
SystemHotkey = "<Ctrl>+<Alt>+<End>"     # System hotkey to exit the script (free text format)
DasHotkeyShort = "%y"                   # Short hotkey to pass into DAS ('+' for Shift, '^' for Ctrl, '%' for Alt)
DasHotkeyLong = "%t"                    # Long hotkey to pass into DAS ('+' for Shift, '^' for Ctrl, '%' for Alt)
SetRisk = 65                            # Set dollar risk per trade here
CurrentPrice = ""                       # Leave blank for MainFunction use
PositionSize = ""                       # Leave blank for MainFunction use
TradeDirection = ""                     # Leave blank for MainFunction use

PrintMessage()

with PynputKeyboard.GlobalHotKeys({
        StartHotkey : MainFunction,
        SystemHotkey : ExitFunction}) as MappedResult:
    MappedResult.join()