import base64, time, threading
import tkinter as tk
from io import BytesIO
from PIL import Image, ImageTk
from control import *

def pic_decode(data):
    return ImageTk.PhotoImage(Image.open(BytesIO(base64.b64decode(data))))

def StartButton(threads, root, base, btn):
#initial
    base.itemconfig(btn[0], state=tk.HIDDEN)
    base.itemconfig(btn[1], state=tk.HIDDEN)
    base.itemconfig(btn[2], state=tk.HIDDEN)
#detect
    while True:
        #mouse position in window
        x = root.winfo_pointerx() - root.winfo_rootx()
        y = root.winfo_pointery() - root.winfo_rooty()
        if((x>=98) and (x<=256) and (y>=194) and (y<=244)):
            base.itemconfig(btn[0], state=tk.HIDDEN)
            base.itemconfig(btn[1], state=tk.DISABLED)
        elif(((x<98) or (x>256) or (y<194) or (y>244))):
            base.itemconfig(btn[0], state=tk.DISABLED)
            base.itemconfig(btn[1], state=tk.HIDDEN)
        #press the button
        if (switch == 1):
            base.itemconfig(btn[0], state=tk.HIDDEN)
            base.itemconfig(btn[1], state=tk.HIDDEN)
            base.itemconfig(btn[2], state=tk.DISABLED)
            time.sleep(0.5)
            threads[2].start()
            break

def prepare(base, btn, cd_num): #after press the button
    base.itemconfig(btn[2], state=tk.HIDDEN)
    base.itemconfig(cd_num[3], state=tk.DISABLED)
    for i in range(3, 0, -1):
        time.sleep(1)
        base.itemconfig(cd_num[i], state=tk.HIDDEN)
        base.itemconfig(cd_num[i-1], state=tk.DISABLED)
    time.sleep(0.5)
    base.itemconfig(cd_num[0], state=tk.HIDDEN)


def initial(threads, base, time_num, cd_num, block_img, next_img): #initial all
    for i in range(4):
        base.itemconfig(cd_num[i], state=tk.HIDDEN)
        for j in range(10):
            base.itemconfig(time_num[i][j], state=tk.HIDDEN)
    base.itemconfig(time_num[0][0], state=tk.DISABLED)
    base.itemconfig(time_num[1][2], state=tk.DISABLED)
    base.itemconfig(time_num[2][0], state=tk.DISABLED)
    base.itemconfig(time_num[3][0], state=tk.DISABLED)
    for k in range(7):
        base.itemconfig(next_img[k], state=tk.HIDDEN)
        for i in range(20):
            for j in range(10):
                base.itemconfig(block_img[k][i][j], state=tk.HIDDEN)

    threads[1].start()

def clock():
    pass