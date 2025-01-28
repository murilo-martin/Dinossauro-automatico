import pyautogui as pya

y_start = 245  
x_start = 760

y_bird = 224

dayTime = False

def bird_there():

    if not dayTime:

        return pya.pixel(765,y_bird)[0] > 50
 
    return pya.pixel(765,y_bird)[0] < 50

pya.moveTo(x_start,y_start)
pya.hotkey('alt', 'tab')
pya.press('space')


while True:
    
    dayTime = pya.pixel(100, y_start)[0] > 50

    # pega possição do mouse
    x, y = pya.position()   

    # pega o valor da posição e indentifica a cor em RGB
    color = pya.pixel(x,y)  
    
    if not dayTime:
    # Se o primeiro valor do RGB for maior que 50
        if(color[0] > 50 or bird_there()):

        # Pressiona Espaço
            pya.press('space')
    
    else:
        if(color[0] < 50 or bird_there()):

        # Pressiona Espaço
            pya.press('space')
               



                                          