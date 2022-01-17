import socket
import threading
from time import sleep

def waitLinked(sock, n):
	while True:
		data = sock.recv(1000).decode("utf8")
		if data.find("linked") != -1:
			print(f"Player{n} Link start!")
			sock.send(b"Start")
			thread = threading.Thread(target = waitStart, args = (sock, n))
			thread.start()
			thread.join()
			break
		else:
			print(f"Player{n} is " + data)
			sleep(1)

def waitStart(sock, n):
	while True:
		data = sock.recv(1000).decode("utf8")
		if data.find("plzSent") != -1:
			print(f"player{n} game start!")
			thread = threading.Thread(target = figthing, args = (sock, n))
			thread.start()
			thread.join()
			break
		sleep(1)

def figthing(sock, n):
	stop = []
	threadS = threading.Thread(target = keepSend, args = (sock, n, stop))
	threadR = threading.Thread(target = keepRecv, args = (sock, n, stop))
	threadS.start()
	threadR.start()
	threadR.join()

def keepSend(sock, n, stop):
	text = f"[[[{n}, {n}, {n}, {n}, {n}]]]"
	while len(stop) == 0:
		sock.send(text.encode('ascii'))
		sleep(1)

def keepRecv(sock, n, stop):
	while True:
		data = sock.recv(1000).decode('utf8')
		print(data)
		try:
			data = eval(data)
			if data["time"] == 0: 
				stop.append("stop")
				break
		except: pass

def main():
	linked = []
	thread = []
	for x in range(10): linked.append("")

	for x in range(len(linked)):
		linked[x] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		linked[x].connect(('192.168.88.128', 9487))
		thread.append(threading.Thread(target = waitLinked, args = (linked[x], x+1)))
		thread[len(thread)-1].start()

	for x in thread: x.join()

if __name__ == "__main__":
	system = threading.Thread(target = main)
	system.start()
	system.join()
