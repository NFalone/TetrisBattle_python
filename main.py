import tkinter as tk
import threading

from pic import *
from func import *
from core import *

def main():
#window basic option
    root = tk.Tk()
    root.title("Tetris Battle")
    pos_window_x = (root.winfo_screenwidth()/2) - (742/2)
    pos_window_y = (root.winfo_screenheight()/2) - (522/2) - 100
    root.geometry('742x522+%d+%d' % (pos_window_x, pos_window_y))
    root.resizable(width=False,height=False)
    base = tk.Canvas(root, height=522, width=742, bg='greenyellow')
    base.config(highlightthickness=0)
    base.pack()
#image load
    pic_back = pic_decode(Background)
    base.create_image(0, 0, anchor=tk.NW, image=pic_back, state=tk.DISABLED)
    btn = [0 for i in range(3)]
    pic_btnStart = pic_decode(button_start)
    btn[0] = base.create_image(177, 220, anchor=tk.CENTER, image=pic_btnStart, state=tk.DISABLED)
    pic_btnHover = pic_decode(button_hover)
    btn[1] = base.create_image(177, 220, anchor=tk.CENTER, image=pic_btnHover, state=tk.DISABLED)
    pic_btnActive = pic_decode(button_active)
    btn[2] = base.create_image(177, 220, anchor=tk.CENTER, image=pic_btnActive, state=tk.DISABLED)
#time image load
    pic_temp = [0 for i in range(10)]
    time_num = [[0 for i in range(10)] for j in range(4)]
    pic_temp[0] = pic_decode(dig0)
    pic_temp[1] = pic_decode(dig1)
    pic_temp[2] = pic_decode(dig2)
    pic_temp[3] = pic_decode(dig3)
    pic_temp[4] = pic_decode(dig4)
    pic_temp[5] = pic_decode(dig5)
    pic_temp[6] = pic_decode(dig6)
    pic_temp[7] = pic_decode(dig7)
    pic_temp[8] = pic_decode(dig8)
    pic_temp[9] = pic_decode(dig9)
    pos = [0, 1, 2.5, 3.5]
    for site in pos:
        for i in range(10):
            time_num[0][i] = base.create_image(307+(35*site), 44, anchor=tk.CENTER, image=pic_temp[i], state=tk.DISABLED)
    pic_colon = pic_decode(colon)
    base.create_image(315+(35*1.5), 44, anchor=tk.CENTER, image=pic_colon, state=tk.DISABLED)

#ready
    base.bind("<Button-1>", go)
    

#threading
    threads = []
    threads.append(threading.Thread(target=StartButton, args=(threads, root, base, btn)))
    threads.append(threading.Thread(target=prepare, args=(base, btn)))

    threads[0].start()

    root.mainloop()

if __name__ == '__main__':
    main()