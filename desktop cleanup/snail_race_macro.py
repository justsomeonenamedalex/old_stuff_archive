import pyautogui as pag
import time

time.sleep(1)
print("Starting")
time.sleep(1)

while True:
    pag.typewrite("!s race 5", interval=0.1)
    pag.press("enter")
    time.sleep(0.002)

    pag.typewrite("!s enter", interval=0.1)
    pag.press("enter")
    time.sleep(0.002)

    time.sleep(5)
