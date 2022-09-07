from turtle import heading, width
import pyautogui

pyautogui.size() # => returns the resolution of the screen

width, heigth = pyautogui.size()

pyautogui.position() # => returns the position of the mouse

pyautogui.moveTo(10,10, duration= 1.5) # => absolute position movement
pyautogui.moveRel(200,0, duration= 2) # => relative movement

# pyautogui.click(<x_position>, <y_position>)
# pyautogui.doubleClick()

# pyautogui.dragRel()