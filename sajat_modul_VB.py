import tkinter as tk

class ButorVB:

    def mozgat_VB(self, x0, y0):
        self.x0 = x0
        self.y0 = y0



class AsztalVB(ButorVB):

    def __init__(self, x0=0,y0=0,x1=300, y1=150, color="brown", tipus="Asztal"):

        self.x0 = x0
        self.y0 = y0
        self.x1= x1
        self.y1= y1
        self.color= color
        self.tipus = tipus



class SzekVB(ButorVB):
    def __init__(self, x0, y0, x1, y1, color, tipus):

        self.x1=150
        self.y1=150
        self.color="black"
        self.tipus = "Szék"

def canvas_hatar_VB(x0, y0, x1, y1, szelesseg, magassag):
    return (
        x0 >= 0
        and y0 >= 0
        and x1 <= szelesseg
        and y1 <= magassag
    )

def utkozes_VB(a, b):
    ax0, ay0, ax1, ay1 = a
    bx0, by0, bx1, by1 = b

    return not (
        ax1 <= bx0
        or ax0 >= bx1
        or ay1 <= by0
        or ay0 >= by1
    )