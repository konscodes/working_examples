import ctypes

def MessageBox(title, text, style):     # Popup message box function
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)