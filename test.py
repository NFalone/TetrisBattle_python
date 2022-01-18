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
# # root.mainloop()
# from bisect import bisect_left 
  
# def binary_search(a, x): 
#     i = bisect_left(a, x) 
#     if i: 
#         return (i) 
#     else: 
#         return -1
  
# # Driver code 
# a  = [0, 2, 6, 7, 9, 11, 15]
# x = int(16) 
# # res = binary_search(a, x) 
# # if res == -1: 
# #     print("There is no value smaller than", x) 
# # else: 
# #     print("Largest value smaller than", x, " is at index", res) 
# # https://ithelp.ithome.com.tw/articles/10254439
# import threading
# import time

# lock = threading.Lock()  # 廁所門的鑰匙(lock)
# toilet = []  # 放屎的馬桶(list)

# # 廁所(function)
# def WC():
#     lock.acquire()  # 使用鑰匙將廁所門上鎖

#     # toilet.append(f"{threading.current_thread().name}: 拉了第1坨屎")  # 將當前的人(線程)所拉的第一屎放進馬桶(list)中
#     st = f"{threading.current_thread().name}: 拉了第1坨屎"
#     toiledadd(st)
#     time.sleep(0.1)
#     # toilet.append(f"{threading.current_thread().name}: 拉了第2坨屎")  # 將當前的人(線程)所拉的第二屎放進馬桶(list)中
#     st = f"{threading.current_thread().name}: 拉了第2坨屎"
#     toiledadd(st)

#     lock.release()  # 將廁所門解鎖, 並把鑰匙放在旁邊等下一個人來拿

# def toiledadd(val):
#     toilet.append(val)

# # 產生3位排隊大號的人
# for i in range(3):
#     wc_thread = threading.Thread(target=WC)
#     wc_thread.start()  # 第 i 個人開始進廁所大號

# time.sleep(1)  # 等待一秒確保三個人都上完廁所, 且馬桶內都有他們排放的屎了
# # print(toilet)  # 將馬桶內的屎打印出來看排序

# a = "123456789"
# print(len(a))
import PGinternet, time
class Test(PGinternet.PGinternet):
    def __keepSend(self):
        while self.__execute:
            while len(self.__willSend) != 0:
                text = str(self.__willSend.pop(0))
                self.__socket.sendall(text.encode('ascii'))
            time.sleep(self.__updateTime)

clss = Test(IP='zephyrouo.ddns.net', host=9487, updateTime=0.005)
clss.link()
block_imgData = [[[0 for i in range(10)] for j in range(20)] for k in range(7)]
clss.send(block_imgData)