from tkinter import *
from PIL import Image, ImageTk
import threading

def main():
    root = Tk()
    root.title('Tetris Battle')
    root.geometry('371x522')
    base = Canvas(root, height=522, width=371, bg='greenyellow')
    base.config(highlightthickness=0) #畫布無邊框
    base.pack()
    #載入 介面 開始按鈕 開始按鈕(被選中) 開始按鈕(按下) 方塊保留mark
    LoadPicture = ['TetrisBattle', 'BackGround', 'start', 'startchoose', 'startdown', 'hold']
    picture = []
    for pic in LoadPicture:
        picture.append(ImageTk.PhotoImage(Image.open(f'.\\pic\\{pic}.png')))

    MarkTB = base.create_image(185.2, 261, anchor=CENTER, image=picture[0], state=DISABLED) 
    BKGD = base.create_image(0, 0, anchor=NW, image=picture[1], state=HIDDEN)
    SB = base.create_image(177, 220, anchor=CENTER, image=picture[2], state=HIDDEN)
    SBC = base.create_image(177, 220, anchor=CENTER, image=picture[3], state=HIDDEN)
    SBD = base.create_image(177, 220, anchor=CENTER, image=picture[4], state=HIDDEN)
    blockhold = base.create_image(45, 115, anchor=CENTER, image=picture[5], state=HIDDEN)
