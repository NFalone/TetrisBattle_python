import tkinter as tk
import threading

from pic import *
from func import *

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
    pic_btnStart = pic_decode(button_start)
    base.create_image(177, 220, anchor=tk.CENTER, image=pic_btnStart, state=tk.DISABLED)
    
    pic_temp = [0 for i in range(10)]
    time_num = [[0 for i in range(10)] for j in range(4)]
    for i in range(10):
        pic_temp[i] = pic_decode(f'dig{i}')
        time_num[0][i] = base.create_image(131+(35*i), 44, anchor=tk.CENTER, image=pic_temp[i], state=tk.DISABLED)

#threading
    threading.Thread()

    root.mainloop()

if __name__ == '__main__':
    main()