import threading
import time, random
from test2 import *
from tkinter import *
from PIL import Image, ImageTk
import numpy as np

root = Tk()
root.title('Tetris Battle')
root.geometry('371x522')
base = Canvas(root, height=522, width=371, bg='greenyellow')
base.config(highlightthickness=0) #畫布無邊框
base.pack()

photo2d = [[0 for i in range(10)] for i in range(5)]
print(photo2d)
photostep = [0 for i in range(10)]
for i in range(10):
    photostep[i] = ImageTk.PhotoImage(Image.open(f'.\\pic\\{i}.png'))
    photo2d[0][i] = base.create_image(30+(35*i), 44, anchor=CENTER, image=photostep[i], state=HIDDEN)
change(base, photo2d)
print(photo2d)
photo2d[3] = [1, 3, 7]
print(photo2d)
print(photo2d[0][4])
for i in photo2d:
    print(i)
photo2dpack = photo2d
for i in photo2dpack:
    print(i)

print(random.randint(0, 7))

root.mainloop()