from base64 import decode
import tkinter as tk
import threading

from control import drop, go, hold_block, left_shift, right_shift, rotate, set_block
from core import  Gaming
from func import StartButton, initial, pic_decode, prepare
from pic import *

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
            time_num[pos.index(site)][i] = base.create_image(307+(35*site), 44, anchor=tk.CENTER, image=pic_temp[i], state=tk.DISABLED)
    pic_colon = pic_decode(colon)
    base.create_image(315+(35*1.5), 44, anchor=tk.CENTER, image=pic_colon, state=tk.DISABLED)
#block image load
    pic_block = [0 for i in range(7)]
    block_img = [[[0 for i in range(10)] for j in range(20)] for k in range(7)]
    remote_block_img = [[[0 for i in range(10)] for j in range(20)] for k in range(7)]
    pic_block[0] = pic_decode(block_red)
    pic_block[1] = pic_decode(block_orange)
    pic_block[2] = pic_decode(block_yellow)
    pic_block[3] = pic_decode(block_green)
    pic_block[4] = pic_decode(block_lightblue)
    pic_block[5] = pic_decode(block_blue)
    pic_block[6] = pic_decode(block_purple)
    for k in range(7):
        for i in range(20):
            for j in range(10):
                block_img[k][i][j] = base.create_image(87+(18*j), 123+(18*i), anchor=tk.NW, image=pic_block[k], state=tk.DISABLED)
                remote_block_img[k][i][j] = base.create_image(457+(18*j), 123+(18*i), anchor=tk.NW, image=pic_block[k], state=tk.DISABLED)
#next image load 292 144
    pic_blocknext = [0 for i in range(7)]
    next_img = [0 for i in range(7)]
    remote_next_img = [0 for i in range(7)]
    pic_blocknext[0] = pic_decode(Z)
    pic_blocknext[1] = pic_decode(L)
    pic_blocknext[2] = pic_decode(Q)
    pic_blocknext[3] = pic_decode(S)
    pic_blocknext[4] = pic_decode(I)
    pic_blocknext[5] = pic_decode(J)
    pic_blocknext[6] = pic_decode(T)
    for i in range(7):
        next_img[i] = base.create_image(292, 144, anchor=tk.NW, image=pic_blocknext[i], state=tk.DISABLED)
        remote_next_img[i] = base.create_image(663, 146, anchor=tk.NW, image=pic_blocknext[i], state=tk.DISABLED)
#hold image load with next
    hold_img = [0 for i in range(7)]
    remote_hold_img = [0 for i in range(7)]
    for i in range(7):
        hold_img[i] = base.create_image(20, 143, anchor=tk.NW, image=pic_blocknext[i], state=tk.DISABLED)
        remote_hold_img[i] = base.create_image(391, 145, anchor=tk.NW, image=pic_blocknext[i], state=tk.DISABLED)
#count down 3 seconds
    pic_temp2 = [0 for i in range(4)]
    cd_num = [0 for i in range(4)]
    pic_temp2[0] = pic_decode(cd0)
    pic_temp2[1] = pic_decode(cd1)
    pic_temp2[2] = pic_decode(cd2)
    pic_temp2[3] = pic_decode(cd3)
    for i in range(4):
        cd_num[i] = base.create_image(177, 220, anchor=tk.CENTER, image=pic_temp2[i], state=tk.DISABLED)

#operate bind
    base.bind("<Button-1>", go) #press the button
    root.bind("<Up>", rotate) #旋轉方塊
    root.bind("<Down>", drop) #下降方塊
    root.bind("<Left>", left_shift) #左移方塊
    root.bind("<Right>", right_shift) #右移方塊
    root.bind("<space>", set_block) #放置方塊
    root.bind("<Shift_L>", hold_block)  #保留方塊
    

#threading
    threads = []
    threads.append(threading.Thread(target=initial, args=(threads, base, time_num, cd_num, block_img, remote_block_img, next_img, remote_next_img, hold_img, remote_hold_img)))
    threads.append(threading.Thread(target=StartButton, args=(threads, root, base, btn)))
    threads.append(threading.Thread(target=prepare, args=(base, btn, cd_num)))
    threads.append(threading.Thread(target=Gaming, args=()))

    threads[0].start()

    root.mainloop()

if __name__ == '__main__':
    main()