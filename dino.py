import pyautogui as pya

while True:

    x, y = pya.position()

    color = pya.pixel(x,y)               

    print("Andando", end="/r")

    if(color[0] > 50):

        pya.press('space')

        print("pulou")