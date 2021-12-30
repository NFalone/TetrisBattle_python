import tkinter as tk

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
    btn_start = pic_decode(button_start)
    base.create_image(177, 220, anchor=tk.CENTER, image=btn_start, state=tk.DISABLED)

    root.mainloop()

if __name__ == '__main__':
    main()