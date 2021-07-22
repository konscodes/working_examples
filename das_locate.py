from pywinauto import Application
import time

start_time = time.time()
time.sleep(5)

app = Application(backend="win32").connect(active_only="True")
#print(app)

MontageWindow = app.window(active_only="True")
MontageWindow.draw_outline()
print("Selecting active Montage window")
time.sleep(3)

Price = MontageWindow.PEdit
Price.draw_outline()
print("Selecting Price field")
time.sleep(3)

Price.type_keys("100", with_spaces = True)
print("Typing in Price field")
time.sleep(3)

print("--- %s seconds ---" % (time.time() - start_time))