import tkinter as tk
import random
import time, asyncio

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
block_imgData = [[[0 for i in range(10)] for j in range(20)] for k in range(7)]

def Gaming(arg_block_img, arg_next_img, arg_base, arg_root):
    global frame_background, frame_backgroundTemp, frame_out, block, block_img, next_img, base, block_next, root
    block_img = arg_block_img
    base = arg_base
    next_img = arg_next_img
    root = arg_root
    frame_background = [[0 for j in range(15)] for i in range(25)] #the frame of background (column 1L4R  row (1T)4B)
    frame_background.append(0)  #frame_background[25] = color info
    frame_backgroundTemp = [[0 for j in range(15)] for i in range(25)] #the status before event
    frame_backgroundTemp.append(0)
    frame_out = [[0 for j in range(15)] for i in range(25)] #after event
    frame_out.append(0)
#create frame edge
    for i in [21, 22, 23, 24]:
        for j in range(15):
            frame_background[i][j] = 1
            frame_backgroundTemp[i][j] = 1
            frame_out[i][j] = 1
    for i in range(25):
        for j in [0, 11, 12, 13, 14]:
            frame_background[i][j] = 1
            frame_backgroundTemp[i][j] = 1
            frame_out[i][j] = 1
#start
    block_next = random.randint(0,6)  #general new block color number(in next)
    base.itemconfig(next_img[block_next], state=tk.DISABLED)
    while get_switch() == 1:
        block_next, block_now = block_generate(block_next)
        block = blockframe[block_site[block_now]]
        asyncio.run(block_merge("game"))
        time.sleep(1000)  #stop

def block_generate(block_next):  #geterate new block color number
    global frame_background, frame_backgroundTemp, frame_out, block_img, base
    set_siteX(4)
    set_siteY(0)
    base.itemconfig(next_img[block_next], state=tk.HIDDEN)
    block_now = block_next
    block_next = random.randint(0,6)
    frame_background[25] = block_now
    frame_backgroundTemp[25] = block_now
    frame_out[25] = block_now
    base.itemconfig(next_img[block_next], state=tk.DISABLED)
    return block_next, block_now

async def block_merge(call):  #merge 2Darray and check the block
    global frame_background, frame_backgroundTemp, frame_out, block_img, base, block_next, block
    for i in range(1, 21):
        for j in range(1, 11):
            frame_out[i][j] = frame_background[i][j]
    x = get_siteX()
    y = get_siteY()
    for i in range(4):
        for j in range(4):
            frame_out[y+i][x+j] = frame_background[y+i][x+j] + block[i][j]
            #merge fail
            if frame_out[y+i][x+j] > 1:
                print("fail")
                if call == "left":
                    set_siteX(get_siteX() + 1)
                    return
                elif call == "right":
                    set_siteX(get_siteX() - 1)
                    return
                elif call == "drop" or call == "set":
                    set_siteY(get_siteY() - 1)
                    #recursive
                    for i in range(1, 21):
                        for j in range(1, 11):
                            frame_out[i][j] = frame_background[i][j]
                    x = get_siteX()
                    y = get_siteY()
                    for i in range(4):
                        for j in range(4):
                            frame_out[y+i][x+j] = frame_background[y+i][x+j] + block[i][j]
                    for i in range(1, 21):
                        for j in range(1, 11):
                            frame_backgroundTemp[i][j] = frame_out[i][j]
                        print(frame_backgroundTemp[i])
                    for i in range(1, 21):
                        for j in range(1, 11):
                            frame_background[i][j] = frame_backgroundTemp[i][j]
                    block_next, block_now = block_generate(block_next)
                    block = blockframe[block_site[block_now]]
                    ScreenUpdate(frame_backgroundTemp)
                    return False
    #merge success
    for i in range(1, 21):
        for j in range(1, 11):
            frame_backgroundTemp[i][j] = frame_out[i][j]
        print(frame_backgroundTemp[i])
    if call == "left" or call == "right" or call == "game":
        ScreenUpdate(frame_backgroundTemp)
    elif call == "drop":
        ScreenUpdate(frame_backgroundTemp)
    return

def block_set(out_merge):  #set and generate
    global frame_background
    x = get_siteX()
    y = get_siteY()
    pass

def ScreenUpdate(frame_backgroundTemp):  #update the image on screen
    global block_img, base, root
    for i in range(20):
        for j in range(10):
            if frame_backgroundTemp[1+i][1+j]-frame_background[1+i][1+j] == 1:
                block_imgData[frame_backgroundTemp[25]][i][j] = 1
            elif frame_backgroundTemp[1+i][1+j]-frame_background[1+i][1+j] == 0 and frame_background[1+i][1+j] == 0:
                block_imgData[frame_backgroundTemp[25]][i][j] = 0
    for k in range(7):
        for i in range(20):
            for j in range(10):
                if block_imgData[k][i][j] == 1:
                    base.itemconfig(block_img[k][i][j], state=tk.DISABLED)
                else:
                    base.itemconfig(block_img[k][i][j], state=tk.HIDDEN)
    root.update()

def timing():  #drop block per second
    time.sleep(1)
    core("drop")

def core(who):
    global threads_merge, frame_backgroundOut, block
    loop = asyncio.get_event_loop()
    if who == "rotate":
        pass
    elif who == "drop":
        set_siteY(get_siteY() + 1)
        tasks = loop.create_task(block_merge("drop"))
    elif who == "left":
        set_siteX(get_siteX() - 1)
        tasks = loop.create_task(block_merge("left"))
    elif who == "right":
        set_siteX(get_siteX() + 1)
        tasks = loop.create_task(block_merge("right"))
    elif who == "set":
        ans = True
        while ans:
            tasks = loop.create_task(block_merge("set"))
    elif who == "hold":
        pass
    loop.run_until_complete(tasks)

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