import pyautogui
import time
import random


screenWidth, screenHeight = pyautogui.size()

pyautogui.moveTo(screenWidth / 2, screenHeight / 2, duration =1)

delay = random.uniform(1, 5)

while True:
    pyautogui.moveRel(0, 10)
    time.sleep(delay)
    pyautogui.moveRel(10, 0)
    time.sleep(delay)
    pyautogui.moveRel(0,-10)
    time.sleep(delay)
    pyautogui.moveRel(-10, 0)
    time.sleep(delay)