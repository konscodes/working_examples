from pywinauto import Application
import time

time.sleep(5)

app = Application(backend="uia").connect(active_only="True")
print(app)

MainWindow = app.window(class_name="Notepad")
print(MainWindow)

TextEditor = MainWindow.Edit0
TextEditor.draw_outline()
print("Selecting TextEditor")
time.sleep(2)

TextEditor.type_keys("Hi from Python interactive prompt", with_spaces = True)
print("Typing in TextEditor")
time.sleep(2)