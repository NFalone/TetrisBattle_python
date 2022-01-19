import base64, time
import tkinter as tk
from io import BytesIO
from PIL import Image, ImageTk

from control import get_switch, set_hold, set_score, set_switch
from PGinternet import PGinternet

net_go = PGinternet(IP='zephyrouo.ddns.net', host=9487, updateTime=0.008)

def pic_decode(data):
    return ImageTk.PhotoImage(Image.open(BytesIO(base64.b64decode(data))))

def StartButton(threads, root, base, btn):
    #initial
    base.itemconfig(btn[0], state=tk.HIDDEN)
    base.itemconfig(btn[1], state=tk.HIDDEN)
    base.itemconfig(btn[2], state=tk.HIDDEN)
    #detect
    while True:
        time.sleep(0.01)
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
        if (get_switch() == 1):
            base.itemconfig(btn[0], state=tk.HIDDEN)
            base.itemconfig(btn[1], state=tk.HIDDEN)
            base.itemconfig(btn[2], state=tk.DISABLED)
            time.sleep(0.5)
            while True:
                time.sleep(0.1)
                if net_go.gameStart:
                    break
            threads[1].start()
            threads[4].start()
            threads[5].start()
            break

IO_go = True
def go(event):
    global IO_go
    if((event.x>=98) and (event.x<=256) and (event.y>=194) and (event.y<=244) and (get_switch() == 0)) and IO_go:
        IO_go = False
        try:
            net_go.link()
        except:
            IO_go = True
        set_switch(1)

def prepare(threads, base, btn, cd_num): #after press the button
    base.itemconfig(btn[2], state=tk.HIDDEN)
    base.itemconfig(cd_num[3], state=tk.DISABLED)
    for i in range(3, 0, -1):
        time.sleep(1)
        base.itemconfig(cd_num[i], state=tk.HIDDEN)
        base.itemconfig(cd_num[i-1], state=tk.DISABLED)
    time.sleep(0.5)
    base.itemconfig(cd_num[0], state=tk.HIDDEN)
    threads[2].start()
    threads[3].start()


def initial(base, time_num, cd_num, block_img, remote_block_img, next_img, remote_next_img, hold_img, remote_hold_img, tick_img, remote_score_num, score_num): #initial all
    global IO_go
    IO_go = True
    for i in range(4):
        base.itemconfig(cd_num[i], state=tk.HIDDEN)
        for j in range(10):
            base.itemconfig(time_num[i][j], state=tk.HIDDEN)
    base.itemconfig(time_num[0][0], state=tk.DISABLED)
    base.itemconfig(time_num[1][2], state=tk.DISABLED)
    base.itemconfig(time_num[2][0], state=tk.DISABLED)
    base.itemconfig(time_num[3][0], state=tk.DISABLED)
    for k in range(7):
        base.itemconfig(hold_img[k], state=tk.HIDDEN)
        base.itemconfig(next_img[k], state=tk.HIDDEN)
        base.itemconfig(remote_hold_img[k], state=tk.HIDDEN)
        base.itemconfig(remote_next_img[k], state=tk.HIDDEN)
        for i in range(20):
            for j in range(10):
                base.itemconfig(block_img[k][i][j], state=tk.HIDDEN)
                base.itemconfig(remote_block_img[k][i][j], state=tk.HIDDEN)
    base.itemconfig(tick_img, state=tk.HIDDEN)
    for i in range(3):
        for j in range(1, 10):
            base.itemconfig(score_num[i][j], state=tk.HIDDEN)
            base.itemconfig(remote_score_num[i][j], state=tk.HIDDEN)
    set_hold(0)
    set_score(0)

def get_netGo():
    global net_go
    return net_go