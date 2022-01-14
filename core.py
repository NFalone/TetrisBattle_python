from ast import arg
from concurrent.futures import thread
import random, threading

from control import *

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

def Gaming(threads, block_img):
    frame_background = [[0 for j in range(15)] for i in range(25)] #the frame of background (column 1L4R  row 1T4B)
    frame_background.append(0)  #frame_background[25] include color info
    frame_backgroundTemp = [[0 for j in range(15)] for i in range(25)]
    frame_backgroundTemp.append(0)
    #location
    site_x = 3
    site_y = 0
    threads[4] = threading.Thread(target=ScreenUpdate, args=(block_img))
    for i in [0, 21, 22, 23, 24]:  #create edge
        for j in [0, 11, 12, 13, 14]:
            frame_background[i][j] = 1
#start
    block_next = random.randint(0,6)  #general new block color number(in next)
    while switch == 1:
        block_now = block_next
        frame_background[25] = block_now
        block = blockframe[block_site[block_now]]
        frame_block = block_merge(frame_background, frame_backgroundTemp, block, site_x, site_y)
        block_next = random.randint(0,6)


def block_merge(frame_background, frame_backgroundTemp, block, site_x, site_y):  #merge 2Darray and check the block
    for i in range(4):
        for j in range(4):
            frame_backgroundTemp[1+site_y+i][1+site_x+j] = frame_background[1+site_y+i][1+site_x+j] + block[i][j]
            if frame_backgroundTemp[1+site_y+i][1+site_x+j] > 1:  #jump over the screen update
                return "JumpOver"
    #else : output the merge result
    return frame_backgroundTemp

def ScreenUpdate(block_img):  #update the image on screen
    for i in range(20):
        for j in range(10):
            pass

def timing():  #move down per second
    pass