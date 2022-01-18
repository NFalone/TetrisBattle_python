#proccess image with another player
"""
11->next
12->score
"""
import time
from tkinter import DISABLED, HIDDEN

from func import get_netGo

net_go = get_netGo()
data_dic = {}
passing = False
def remote():
    global data_dic, passing
    while True:
        time.sleep(0.005)
        data_str = net_go.recv()
        if data_str!="" and data_str.find("{")!=-1 and data_str.find("}")!=-1:
            if data_str.find("{") < data_str.find("}"):
                data_str = data_str[data_str.find("{") : data_str.find("}")+1]
                data_dic = eval(data_str)
                print("echo", data_dic)
                passing = True

def remoteScreen(root, base, remote_block_img, remote_next_img, remote_score_num, time_num):
    global data_dic, passing
    while True:
        time.sleep(0.003)
        if passing:
            data = eval(data_dic['data'])
            if data !="":
                print("pass_before", data, type(data))
                now = data_dic['time']
                if type(data) == list:
                    if data[0]!=11 and data[0]!=12 and len(data)>1:
                        print("pass_after", data, type(data))
                    # if data[0] == 11:
                    #     for i in range(7):
                    #         base.itemconfig(remote_next_img[i], state=HIDDEN)
                    #     base.itemconfig(remote_next_img[data[1]], state=DISABLED)
                    # elif data[0] == 12:
                    #     score = data[1]
                    #     for i in range(3):
                    #         for j in range(10):
                    #             base.itemconfig(remote_score_num[i][j], state=HIDDEN)
                    #     base.itemconfig(remote_score_num[0][(score%1000)//100], state=DISABLED)
                    #     base.itemconfig(remote_score_num[1][(score%100)//10], state=DISABLED)
                    #     base.itemconfig(remote_score_num[2][(score%10)//1], state=DISABLED)
                    # else:
                    #     for k in range(7):
                    #         for i in range(20):
                    #             for j in range(10):
                    #                 if data[k][i][j] == 1:
                    #                     base.itemconfig(remote_block_img[k][i][j], state=DISABLED)
                    #                 else:
                    #                     base.itemconfig(remote_block_img[k][i][j], state=HIDDEN)
                    # for i in range(3): #minutes
                    #     base.itemconfig(time_num[1][i], state=HIDDEN)
                    # base.itemconfig(time_num[1][now//60], state=DISABLED)
                    # for i in range(10): #seconds
                    #     base.itemconfig(time_num[2][i], state=HIDDEN)
                    #     base.itemconfig(time_num[3][i], state=HIDDEN)
                    # base.itemconfig(time_num[2][(now%60)//10], state=DISABLED)
                    # base.itemconfig(time_num[3][(now%60)%10], state=DISABLED)
                    # root.update()
                    # passing = False