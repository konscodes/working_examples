'''
GUI automation script to suplement DAS hotkey

Idea: calculate stop distance based on current position size and set dollar risk

DAS hotkey script (Short): 
CXL ALLSYMB;SwitchTWnd;Route=Stop;Share=Pos;StopPrice=50/Pos;StopPrice=AvgCost-StopPrice;StopType=MARKET;TIF=DAY;SELL=Send;

Problem: DAS scripting language doesnt support Risk/Position opperation; moreover DAS API is 100$ per month
Solution: read montage controls with python library for GUI automation pywinauto; perform calculation in python; return desired value;
Script will put the new stop distance in Price field and hit the hotkey to send the order

Requirements:
- Pythin 3.8.0
- Pywinauto 0.6.8

Preparation:
1. Set key combination in python to start calculations
2. Add the following hotkey to DAS (Short)
CXL ALLSYMB;SwitchTWnd;Route=Stop;StopPrice=AvgCost-Price;StopType=MARKET;TIF=DAY;SELL=Send;
3. Set key combination in python for your DAS hotkey
4. Set your dollar risk in python script
5. Run the script

How to use:
1. Make sure that montage window is active
2. Hit the hotkey defined in Preparation Step1
3. Profit ;) the correct order should be placed

Additional note: if there are many montage windows in use all of them should be in popout mode (right click the header --> pop out)
'''

from pywinauto import Application
import time

time.sleep(5) # debug wait to select active window
print("Starting execution now \n")

# Add error handling
# Add waiting for key press function to activate python script

# Connect to active app
app = Application(backend="win32").connect(active_only="True")

# Select active window
MontageWindow = app.window(active_only="True")

# Define controls (Need P button, Shares field, Price field)
PositionButton = MontageWindow.P
PositionButton.draw_outline()

Price = MontageWindow.PEdit
Price.draw_outline()

Shares = MontageWindow.Edit2
Shares.draw_outline()

# Define functions and their variables
CurrentPosition = ""
CurrentPrice = ""

def GetMontageVariables():
    global CurrentPosition
    global CurrentPrice
    CurrentPrice = Price.get_line(0)
    #PositionButton.click()
    CurrentPosition = Shares.get_line(0)
    print("Current Price: ", CurrentPrice)
    print("Current Position: ", CurrentPosition)
    return CurrentPosition

# Get current variables
print("\n Original: ")
GetMontageVariables()

# Define user variables
SetRisk = 65 # Set dollar risk per trade here

# Perform calculations
StopDistance = (SetRisk/int(CurrentPosition))
print("\nCalculated StopDistance: ", StopDistance)

# Replace variables
Price.set_edit_text(StopDistance) # Set variable value
print("\n After change: ")
GetMontageVariables()