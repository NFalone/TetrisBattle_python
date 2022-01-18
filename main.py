import tkinter as tk
import threading

from gaming import Gaming, drop, hold_block, left_shift, right_shift, rotate, set_block, timing
from func import StartButton, go, initial, pic_decode, prepare
from pic import *
from remote import remote, remoteScreen

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
    pic_tick = pic_decode(tick)
    tick_img = base.create_image(28, 93, anchor=tk.NW, image=pic_tick, state=tk.DISABLED)
#time image load
    pic_temp = [0 for i in range(10)]
    time_num = [[0 for i in range(10)] for j in range(4)]
    dig = [dig0, dig1, dig2, dig3, dig4, dig5, dig6, dig7, dig8, dig9]
    for i in range(10):
        pic_temp[i] = pic_decode(dig[i])
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
    colorblock = [block_red, block_orange, block_yellow, block_green, block_lightblue, block_blue, block_purple]
    for i in range(7):
        pic_block[i] = pic_decode(colorblock[i])
    for k in range(7):
        for i in range(20):
            for j in range(10):
                block_img[k][i][j] = base.create_image(87+(18*j), 123+(18*i), anchor=tk.NW, image=pic_block[k], state=tk.DISABLED)
                remote_block_img[k][i][j] = base.create_image(457+(18*j), 123+(18*i), anchor=tk.NW, image=pic_block[k], state=tk.DISABLED)
#next image load 292 144
    pic_blocknext = [0 for i in range(7)]
    next_img = [0 for i in range(7)]
    remote_next_img = [0 for i in range(7)]
    zlqsijt = [Z, L, Q, S, I, J, T]
    for i in range(7):
        pic_blocknext[i] = pic_decode(zlqsijt[i])
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
    
#score image load
    small_num = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
    pic_digL = [0 for i in range(10)]
    score_num = [[0 for j in range(10)] for i in range(3)]
    remote_score_num = [[0 for j in range(10)] for i in range(3)]
    for i in range(10):
        pic_digL[i] = pic_decode(small_num[i])
    for i in range(3):
        for j in range(10):
            score_num[i][j] = base.create_image(26+(i*20), 337, anchor=tk.CENTER, image=pic_digL[j], state=tk.DISABLED)
    for i in range(3):
        for j in range(10):
            remote_score_num[i][j] = base.create_image(397+(i*20), 339, anchor=tk.CENTER, image=pic_digL[j], state=tk.DISABLED)

#start button image load
    btn = [0 for i in range(3)]
    pic_btnStart = pic_decode(button_start)
    btn[0] = base.create_image(177, 220, anchor=tk.CENTER, image=pic_btnStart, state=tk.DISABLED)
    pic_btnHover = pic_decode(button_hover)
    btn[1] = base.create_image(177, 220, anchor=tk.CENTER, image=pic_btnHover, state=tk.DISABLED)
    pic_btnActive = pic_decode(button_active)
    btn[2] = base.create_image(177, 220, anchor=tk.CENTER, image=pic_btnActive, state=tk.DISABLED)


#operate bind
    root.bind("<Button-1>", go) #press the button
    root.bind("<Up>", rotate) #旋轉方塊
    root.bind("<Down>", drop) #下降方塊
    root.bind("<Left>", left_shift) #左移方塊
    root.bind("<Right>", right_shift) #右移方塊
    root.bind("<space>", set_block) #放置方塊
    root.bind("<Shift_L>", hold_block)  #保留方塊 bug
    

#threading
    threads = []
    threads.append(threading.Thread(target=StartButton, args=(threads, root, base, btn)))
    threads.append(threading.Thread(target=prepare, args=(threads, base, btn, cd_num)))
    threads.append(threading.Thread(target=Gaming, args=(block_img, next_img, base, root, tick_img, hold_img, score_num, threads)))
    threads.append(threading.Thread(target=timing, args=()))
    threads.append(threading.Thread(target=remote, args=()))
    threads.append(threading.Thread(target=remoteScreen, args=(root, base, remote_block_img, remote_next_img, remote_score_num, time_num)))
    threads.append(threading.Thread(target=initial, args=(threads, base, time_num, cd_num, block_img, remote_block_img, next_img, remote_next_img, hold_img, remote_hold_img, tick_img, remote_score_num, score_num)))

    initial(threads, base, time_num, cd_num, block_img, remote_block_img, next_img, remote_next_img, hold_img, remote_hold_img, tick_img, remote_score_num, score_num)
    threads[0].start()
    root.mainloop()

if __name__ == '__main__':
    main()