import tkinter
import math
from random import randint

tick = 1
MS = 1
WIDTH = 600
HEIGHT = 600
XMOD = 0
YMOD = 0
X, Y = 0, 0
C = 0
#prime ratio 2538/22700
def is_prime(num):
    return 2538 > randint(0,22700)
    

def hexify(x:int,y:int,z:int) -> "HEXCODE":
    returnstring = (hex(x)[-2:]).upper() + (hex(y)[-2:]).upper() + (hex(z)[-2:]).upper()
    returnstring = returnstring.replace("X", "0")
    return "#" + returnstring

def colorSweep(num:int) -> "HEXCODE":
    "Takes an integer and returns a hexcode color"
    frac = (num//256) % 6
    over = num%256
    anti = 255-over
    if frac == 0:
        return hexify(255, over, 0)
    if frac == 1:
        return hexify(anti, 255, 0)
    if frac == 2:
        return hexify(0, 255, over)
    if frac == 3:
        return hexify(0, anti, 255)
    if frac == 4:
        return hexify(over, 0, 255)
    if frac == 5:
        return hexify(255, 0, anti)
    
    
    

class Animation:
    def __init__(self):
        global MS
        self._window = tkinter.Tk()
        self._canvas = tkinter.Canvas(
            master = self._window, width = WIDTH, height = HEIGHT,
            background = "#000000")
        self._canvas.grid(row = 0, column = 0)
        self._window.after(MS, self._next)
        self._window.mainloop()
    def _next(self):
        global MS, tick, WIDTH, HEIGHT, XMOD, YMOD, X, Y, C
        #X = math.cos(tick*math.pi/2)*tick
        #Y = math.sin(tick*math.pi/2)*tick
        if (tick == 1):
            X, Y = 0, 0
        elif(tick == 2):
            X, Y = 1, 0
            YMOD = 1
            C = YMOD
        elif (XMOD > 0):
            X = X + 1
            C = C-1
            if (C == 0):
                YMOD = XMOD
                XMOD = 0
                C = YMOD
        elif (YMOD > 0):
            Y = Y + 1
            C = C-1
            if (C == 0):
                XMOD = -YMOD -1
                YMOD = 0
                C = XMOD
        elif (XMOD < 0):
            X = X - 1
            C = C+1
            if (C == 0):
                YMOD = XMOD
                XMOD = 0
                C = YMOD
        elif (YMOD < 0):
            Y = Y - 1
            C = C+1
            if (C == 0):
                XMOD = -YMOD + 1
                YMOD = 0
                C = XMOD

        if (is_prime(tick)):
            self._canvas.create_rectangle(WIDTH/2 - 2+X*4, HEIGHT/2 - 2+Y*4, 
                                      WIDTH/2 + 2+X*4, HEIGHT/2 + 2+Y*4,
                                      fill = "white")
        if (tick == 1):
            self._canvas.create_rectangle(WIDTH/2 - 2+X*4, HEIGHT/2 - 2+Y*4, 
                                      WIDTH/2 + 2+X*4, HEIGHT/2 + 2+Y*4,
                                      fill = "red")
        tick += 1
        if tick < 22700:
            self._window.after(MS, self._next)
        else:
            print("Done!")

Animation()
