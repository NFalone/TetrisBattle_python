import tkinter as tk
import random
import time, asyncio

from control import get_hold, get_holdCount, get_siteX, get_siteY, get_switch, set_hold, set_holdCount, set_siteX, set_siteY
from pic import T

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
part = {"0":1, "1":0, "2":3, "3":4, "4":5, "5":2, "6":6, "7":8, "8":7, "9":10, "10":9, "11":12, "12":13, "13":14, "14":11, "15":16, "16":17, "17":18, "18":15}
part2 = {"1":0, "0":1, "3":2, "4":3, "5":4, "2":5, "6":6, "8":7, "7":8, "10":9, "9":10, "12":11, "13":12, "14":13, "11":14, "16":15, "17":16, "18":17, "15":18}
block_imgData = [[[0 for i in range(10)] for j in range(20)] for k in range(7)]

def Gaming(arg_block_img, arg_next_img, arg_base, arg_root, arg_tick_img, arg_hold_img):
    global frame_background, frame_backgroundTemp, frame_out, block_img, next_img, base, block_next, root, block_now, blockStatus, tick_img, hold_img
    block_img = arg_block_img
    base = arg_base
    next_img = arg_next_img
    root = arg_root
    tick_img = arg_tick_img
    hold_img = arg_hold_img
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
        time.sleep(1000)  #stop

def block_generate(block_next):  #geterate new block color number and update image
    global frame_background, frame_backgroundTemp, frame_out, block_img, base, blockStatus, block
    set_siteX(4)
    set_siteY(0)
    set_holdCount(0)
    base.itemconfig(next_img[block_next], state=tk.HIDDEN)
    block_now = block_next
    block_next = random.randint(0,6)
    frame_background[25] = block_now
    frame_backgroundTemp[25] = block_now
    frame_out[25] = block_now
    base.itemconfig(next_img[block_next], state=tk.DISABLED)
    blockStatus = block_site[block_now]
    block = blockframe[blockStatus]
    #update image
    for i in range(1, 21):
        for j in range(1, 11):
            frame_out[i][j] = frame_background[i][j]
    x = get_siteX()
    y = get_siteY()
    for i in range(4):
        for j in range(4):
            frame_out[y+i][x+j] = frame_background[y+i][x+j] + block[i][j]
    ScreenUpdate(frame_out)
    return block_next, block_now

async def block_merge(call):  #merge 2Darray and check the block
    global frame_background, frame_backgroundTemp, frame_out, block_img, base, block_next, block, part2, block_now, block, blockStatus
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
                    ScreenUpdate(frame_backgroundTemp)
                    for i in range(1, 21):
                        for j in range(1, 11):
                            frame_background[i][j] = frame_backgroundTemp[i][j]
                    block_next, block_now = block_generate(block_next)
                    block = blockframe[block_site[block_now]]
                    return False
                elif call == "rotate":
                    blockStatus = part2[str(blockStatus)]
                    block = blockframe[blockStatus]
                    return
    #merge success
    for i in range(1, 21):
        for j in range(1, 11):
            frame_backgroundTemp[i][j] = frame_out[i][j]
        print(frame_backgroundTemp[i])
    if call == "left" or call == "right" or call == "game":
        ScreenUpdate(frame_backgroundTemp)
    elif call == "drop":
        ScreenUpdate(frame_backgroundTemp)
    elif call == "rotate":
        ScreenUpdate(frame_backgroundTemp)
    elif call == "set":
        return True
    return

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
    while get_switch() == 1:
        time.sleep(1)
        set_siteY(get_siteY() + 1)
        asyncio.run(block_merge("drop"))

# async def tick():
#     global tick_img, base
#     if get_holdCount()==0:
#         base.itemconfig(tick_img, state=tk.DISABLED)
#         root.update()
#         await asyncio.sleep(0.5)
#         base.itemconfig(tick_img, state=tk.HIDDEN)
# hold_temp = 0
# def tick_proccess():
#     global frame_backgroundTemp, hold_img, block_site, base, blockStatus, block, block_next, block_now, root, hold_temp
#     temp = frame_backgroundTemp[25]
#     if get_hold() == 0:
#         set_hold(1)
#         hold_temp = temp
#         base.itemconfig(hold_img[hold_temp], state=tk.DISABLED)
#         block_next, block_now = block_generate(block_next)
#         return
#     elif get_hold() == 1:
#         if get_holdCount() == 0:
#             set_holdCount(1)
#             frame_backgroundTemp[25] = hold_temp
#             base.itemconfig(hold_img[hold_temp], state=tk.HIDDEN)
#             hold_temp = temp
#             base.itemconfig(hold_img[hold_temp], state=tk.DISABLED)
#             blockStatus = block_site[frame_backgroundTemp[25]]
#             block = blockframe[blockStatus]
#             #update image
#             for i in range(1, 21):
#                 for j in range(1, 11):
#                     frame_out[i][j] = frame_background[i][j]
#             frame_out[25] = frame_backgroundTemp[25]
#             # ScreenUpdate(frame_out)
#             x = get_siteX()
#             y = get_siteY()
#             for i in range(4):
#                 for j in range(4):
#                     frame_out[y+i][x+j] = frame_background[y+i][x+j] + block[i][j]
#             ScreenUpdate(frame_out)

def core(who):
    global threads_merge, frame_backgroundOut, block, block_now, block_site, part, blockStatus, tick_img
    loop = asyncio.get_event_loop()
    if who == "rotate":
        blockStatus = part[str(blockStatus)]
        block = blockframe[blockStatus]
        tasks = loop.create_task(block_merge("rotate"))
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
            set_siteY(get_siteY() + 1)
            tasks_set = loop.create_task(block_merge("set"))
            loop.run_until_complete(tasks_set)
            ans = tasks_set.result()
        return
    # elif who == "hold":
    #     tasks_hold = loop.create_task(tick())
    #     loop.run_until_complete(tasks_hold)
    #     tick_proccess()
    #     return
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

# def hold_block(event):  #shift
#     if get_switch() == 0:
#         return
#     core("hold")