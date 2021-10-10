#!/usr/bin/python3.6
import numpy as np
import scipy.stats
import math
import string
import sys
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.animation import FuncAnimation
from ball import *
from tkinter import *
import time


window = Tk()
WIDTH = 500 
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height = HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0, 0, 100, 1, 1, "white")
tennis_ball = Ball(canvas, 0, 0, 60, 4, 2, "green")
cricket_ball = Ball(canvas, 0, 0, 50, 8, 7, "red")
squash_ball = Ball(canvas, 0, 0, 30, 10, 30, 'black' )


while True:
    volley_ball.move()
    tennis_ball.move()
    cricket_ball.move()
    squash_ball.move()

    window.update()
    time.sleep(0.01)


window.mainloop()


