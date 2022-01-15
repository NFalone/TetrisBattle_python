import tkinter as tk
import random, threading

from control import get_siteX, get_siteY, get_switch, set_siteX, set_siteY

blockframe = [[[0, 0, 0, 0],  #block0 紅Z  0
               [0, 1, 1, 0],
               [0, 0, 1, 1],
               [0, 0, 0, 0]],
              [[0, 0, 1, 0],
               [0, 1, 1, 0],
               [0, 1, 0, 0],
               [0, 0, 0, 0]],

              [[0, 0, 0, 0],  #block1 菊L  2
               [0, 0, 1, 0],
               [1, 1, 1, 0],
               [0, 0, 0, 0]],
              [[1, 0, 0, 0],
               [1, 0, 0, 0],
               [1, 1, 0, 0],
               [0, 0, 0, 0]],
              [[0, 0, 0, 0],
               [1, 1, 1, 0],
               [1, 0, 0, 0],
               [0, 0, 0, 0]],
              [[1, 1, 0, 0],
               [0, 1, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 0, 0]],

              [[0, 0, 0, 0],  #block2 黃Q  6
               [0, 1, 1, 0],
               [0, 1, 1, 0],
               [0, 0, 0, 0]],

              [[0, 0, 0, 0],  #block3 綠S  7
               [0, 1, 1, 0],
               [1, 1, 0, 0],
               [0, 0, 0, 0]],
              [[0, 1, 0, 0],
               [0, 1, 1, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 0]],

              [[0, 0, 0, 0],  #block4 水藍I  9
               [1, 1, 1, 1],
               [0, 0, 0, 0],
               [0, 0, 0, 0]],
              [[0, 1, 0, 0],
               [0, 1, 0, 0],
               [0, 1, 0, 0],
               [0, 1, 0, 0]],

              [[0, 0, 0, 0],  #block5 藍J  11
               [1, 0, 0, 0],
               [1, 1, 1, 0],
               [0, 0, 0, 0]],
              [[0, 1, 1, 0],
               [0, 1, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 0, 0]],
              [[0, 0, 0, 0],
               [1, 1, 1, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 0]],
              [[0, 1, 0, 0],
               [0, 1, 0, 0],
               [1, 1, 0, 0],
               [0, 0, 0, 0]],

              [[0, 1, 0, 0],  #block6 紫T  15
               [1, 1, 1, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]],
              [[0, 1, 0, 0],
               [0, 1, 1, 0],
               [0, 1, 0, 0],
               [0, 0, 0, 0]],
              [[0, 0, 0, 0],
               [1, 1, 1, 0],
               [0, 1, 0, 0],
               [0, 0, 0, 0]],
              [[0, 1, 0, 0],
               [1, 1, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 0, 0]]]
block_site = [0, 2, 6, 7, 9, 11, 15]

def Gaming(block_img, base):
    global frame_background, frame_backgroundTemp, threads_merge, threads_screen
    frame_background = [[0 for j in range(15)] for i in range(25)] #the frame of background (column 1L4R  row 1T4B)
    frame_background.append(0)  #frame_background[25] = color info
    frame_backgroundTemp = [[0 for j in range(15)] for i in range(25)] #the status before event
    frame_backgroundTemp.append(0)
    frame_backgroundOut = [[0 for j in range(15)] for i in range(25)] #after event
    frame_backgroundOut.append(0)
    #declare variable for threading to passing argument
    block = blockframe[0]
    threads_merge = threading.Thread(target=block_merge, args=(block, frame_backgroundOut))
    threads_screen = threading.Thread(target=ScreenUpdate, args=(frame_backgroundTemp, block_img, base))
    for i in [0, 21, 22, 23, 24]:  #create edge
        for j in [0, 11, 12, 13, 14]:
            frame_background[i][j] = 1
#start
    block_next = random.randint(0,6)  #general new block color number(in next)
    while get_switch() == 1:
        blocknext, block_now = block_generate(block_next)
        block = blockframe[block_site[block_now]]
        block_merge(block, frame_backgroundOut)

def block_generate(block_next):  #geterate new block color number
    global frame_background, frame_backgroundTemp
    set_siteX(4)
    set_siteY(1)
    block_now = block_next
    block_next = random.randint(0,6)
    frame_background[25] = block_now
    frame_backgroundTemp[25] = block_now
    return block_next, block_now

def block_merge(block, frame_backgroundOut):  #merge 2Darray and check the block
    global frame_background, frame_backgroundTemp, threads_screen
    x = get_siteX()
    y = get_siteY()
    for i in range(4):
        for j in range(4):
            frame_backgroundOut[y+i][x+j] = frame_background[y+i][x+j] + block[i][j]
            #merge fail
            if frame_backgroundOut[y+i][x+j] > 1:  #jump over the screen update
                return "JumpOver"
    #merge success
    for i in range(25):
        for j in range(15):
            frame_backgroundTemp[i][j] = frame_backgroundOut[i][j]
    threads_screen.start()

def block_set(out_merge):
    global frame_background
    x = get_siteX()
    y = get_siteY()
    pass

def ScreenUpdate(frame_backgroundTemp, block_img, base):  #update the image on screen
    if frame_backgroundTemp == "JumpOver":
        return
    else:
        for i in range(20):
            for j in range(10):
                base.itemconfig(block_img[frame_backgroundTemp[25]][i][j], status=tk.DISABLED)

def timing():  #move down per second
    pass

def core(who):
    global threads_merge
    if who == "rotate":
        pass
    elif who == "drop":
        set_siteY(get_siteY() + 1)
        pass
    elif who == "left":
        set_siteX(get_siteX() - 1)
        threads_merge.start()
        pass
    elif who == "right":
        set_siteX(get_siteX() + 1)
        pass
    elif who == "set":
        pass
    elif who == "hold":
        pass

#game operate
def rotate(event):  #up
    if get_switch() == 0:
        return
    core("rotate")

def drop(event):  #down
    if get_switch() == 0:
        return
    core("drop")

def left_shift(event):  #left
    if get_switch() == 0:
        return
    core("left")

def right_shift(event):  #right
    if get_switch() == 0:
        return
    core("right")

def set_block(event):  #space
    if get_switch() == 0:
        return
    core("set")

def hold_block(event):  #shift
    if get_switch() == 0:
        return
    core("hold")