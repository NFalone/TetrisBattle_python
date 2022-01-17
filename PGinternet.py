import socket
from time import sleep
from threading import Thread


class PGinternet():
	def __init__(self, updateTime = 1):
		self.__done = True
		self.__execute = True 
		self.__getRecv = []
		self.__willSend = []
		self.__updateTime = int(updateTime)
		self.__connect_num = 1

	def start(self):
		if 1 > self.__connect_num: raise PGerror("connect num must more than 0.")

		self.__done = False
		system = Thread(target = self.__control)
		system.start()
		self.__done = True

	def __control(self):
		linked = []
		thread = []
		for x in range(self.connect_num): linked.append("")

		for x in range(self.connect_num):
			linked[x] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			linked[x].connect(('192.168.88.128', 9487))
			thread.append(Thread(target = self.__waitLinked, args = (linked[x], x+1)))
			thread[len(thread)-1].start()

		#for x in thread: x.join()

	def __waitLinked(self, sock, n):
		while True:
			data = sock.recv(1000).decode("utf8")
			if data.find("linked") != -1:
				sock.send(b"Start")
				thread = Thread(target = self.__waitStart, args = (sock, n))
				thread.start()
				break
			else: sleep(self.__updateTime)

	def __waitStart(self, sock, n):
		while True:
			data = sock.recv(1000).decode("utf8")
			if data.find("plzSent") != -1:
				thread = Thread(target = self.__figthing, args = (sock, n))
				thread.start()
				break
			sleep(self.__updateTime)

	def __figthing(self, sock, n):
		self.__execute = True
		threadS = Thread(target = self.__keepSend, args = (sock, n))
		threadR = Thread(target = self.__keepRecv, args = (sock, n))
		threadS.start()
		threadR.start()

	def __keepSend(self, sock, n):
		while self.__execute:
			while len(self.__willSend) != 0:
				text = str(self.__willSend.pop(0))
				sock.send(text.encode('ascii'))
			sleep(self.__updateTime)

	def __keepRecv(self, sock, n):
		while True:
			data = sock.recv(1000).decode('utf8')
			self.__getRecv.append(data)
			try:
				data = eval(data)
				if data["time"] == 0:
					self.__execute = False
					break
			except: pass
			sleep(self.__updateTime)

	def send(self, text): self.__willSend.append(text)

	def recv(self) -> str:
		ans = ""
		while len(self.__getRecv) != 0:
			ans += self.__getRecv.pop(0)
		return ans

	@property
	def done(self) -> bool: return self.__execute

	@property
	def connect_num(self) -> int: return self.__connect_num

	@property
	def updateTime(self) -> int: return self.__updateTime

	@updateTime.setter
	def updateTime(self, newTime):
		if 0 >= self.__updateTime: raise PGerror("update time must more than 0.")
		self.updateTime = int(newTime)

class PGerror(Exception):
    def __init__(self, Error):
        super().__init__(self)
        self.error = Error

    def __str__(self):
        return self.error


if __name__ == "__main__":
	net = PGinternet(updateTime = 1)
	net.start()
	#net.updateTime = 1

	while net.done:
		net.send("[[[[[77777777777]]]]]")
		data = net.recv()
		print(data)
		sleep(1)