import time
import pyautogui as pya


while True:
    
    time.sleep(1)

    x, y = pya.position()

    print(x,y)