import pyautogui

pyautogui.typewrite("Hello World", interval= 0.2)

pyautogui.typewrite(["a", "b", "left", "left", "X", "Y"], interval= 0.2)

# key combinations:
pyautogui.hotkey("ctrl", "o")