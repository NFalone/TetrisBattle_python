import socket
from time import sleep

linked = [""] * 2

for x in range(2): linked[x] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for x in range(2): linked[x].connect(('192.168.88.128', 80))

while True:
    data = linked[0].recv(1000)
    data = data.decode("utf8")
    if data.find("linked") != -1: 
        print("Player1 Link start!")
        break
    else: 
        print("Player1 is " + data)
        sleep(1)
        
while True:
    data = linked[1].recv(1000)
    data = data.decode("utf8")
    if data.find("linked") != -1:
        print("Player2 Link start!")
        break
    else:
        print("Player2 is " + data)
        sleep(1)

linked[0].send(b"Start")
linked[1].send(b"Start")
    
while True:
    data = linked[0].recv(1000)
    data = data.decode("utf8")
    if data.find("plzSent") != -1:
        print("gameStart!")
        break

while True:
    data = linked[1].recv(1000)
    data = data.decode("utf8")
    if data.find("plzSent") != -1:
        print("gameStart!")
        break
    
while True:
    linked[0].send(b"[[[77777777777]]]")
    linked[1].send(b"[[[8]]]")
    print(linked[0].recv(1000).decode('utf8'))
    
    linked[1].send(b"[[[8]]]")
    sleep(1)
    print(linked[1].recv(1000).decode('utf8'))
