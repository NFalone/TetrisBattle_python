import base64, time
import tkinter as tk
from io import BytesIO
from PIL import Image, ImageTk
from core import *

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
        
        if (get_switch() == 1):
            base.itemconfig(btn[0], state=tk.HIDDEN)
            base.itemconfig(btn[1], state=tk.HIDDEN)
            base.itemconfig(btn[2], state=tk.DISABLED)
            time.sleep(0.5)
            threads[1].start()
            break

def prepare(base, btn):
    pass