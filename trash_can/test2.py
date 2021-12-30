import threading
import time
from tkinter import *
from PIL import Image, ImageTk
import numpy as np

def change(base, photo2d):
    base.itemconfig(photo2d[0][4], state = DISABLED)
    base.itemconfig(photo2d[0][7], state = DISABLED)
    base.itemconfig(photo2d[1][8], state = DISABLED)
