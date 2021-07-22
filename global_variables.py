CurrentPosition = ""

def GetMontageVariables():
    global CurrentPosition
    CurrentPrice = 1
    CurrentPosition = 2
    print(CurrentPosition)
    return CurrentPrice, CurrentPosition
    

GetMontageVariables()
print(CurrentPosition)
