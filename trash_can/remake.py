from tkinter import *
from main import get_startLD


def ReMake(base, ucd1, ucd2, ucd3):
    # clock
    for i in range(10):
        base.itemconfig(ucd3[i], state=HIDDEN)
    for i in range(6):
        base.itemconfig(ucd2[i], state=HIDDEN)
    for i in range(3):
        base.itemconfig(ucd1[i], state=HIDDEN)
    
    startLOAD = get_startLD()
    startLOAD.start()