# array3d = [[[0 for i in range(5)] for j in range(5)] for k in range(5)]
# #3d, 2d, 1d
# array3d[1][2][0] = 77

# print(array3d[1])

# array2d = [[0 for i in range(5)] for j in range(5)]
# array2d[0][1] = 77

# print(array2d)
# array2d.append(0)
# print(array2d)

# def chvar(x):
#     x = 10
#     z = 10
#     return x, z

# x = 5
# y = chvar(x)
# print(x, type(y))

# a, b = y
# print(a, b)
# from tkinter import *
# def keyup(event):
#     print('up', event.char)
# def keydown(event):
#     print('down', event.char)
# root = Tk()
# frame = Frame(root, width=100, height=100)
# frame.bind("<Down>", keydown)
# frame.bind("<KeyRelease>", keyup)
# frame.pack()
# frame.focus_set()
# root.mainloop()
from bisect import bisect_left 
  
def binary_search(a, x): 
    i = bisect_left(a, x) 
    if i: 
        return (i-1) 
    else: 
        return -1
  
# Driver code 
a  = [0, 2, 6, 7, 9, 11, 15]
x = int(7) 
res = binary_search(a, x) 
if res == -1: 
    print("There is no value smaller than", x) 
else: 
    print("Largest value smaller than", x, " is at index", res) 