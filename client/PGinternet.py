import socket
from time import sleep
from threading import Thread


class PGinternet():
	def __init__(self, updateTime = 1, IP = "127.0.0.1", host = 80):
		self.__socket = None
		self.__execute = True
		self.__linkedserver = False
		self.__getRecv = []
		self.__willSend = []
		self.__serverAt = (IP, host)
		self.__updateTime = int(updateTime)

	def link(self):
		self.__linkedserver = False
		system = Thread(target = self.__control)
		system.start()

	def __control(self):
		self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		for linktimes in range(10):
			try:
				self.__socket.connect(self.__serverAt)
				break
			except: sleep(0.5)
		else:
			raise PGerror("The server block this request link")
		self.__socket.setblocking(False)
				
		thread = Thread(target = self.__waitLinked)
		thread.start()

	def __waitLinked(self):
		while True:
			try:
				data = self.__socket.recv(1000).decode("utf8")
				if data.find("linked") != -1:
					self.__socket.send(b"Start")
					thread = Thread(target = self.__waitStart)
					thread.start()
					break
				else: sleep(self.__updateTime)
			except: sleep(self.__updateTime)

	def __waitStart(self):
		while True:
			try:
				data = self.__socket.recv(1000).decode("utf8")
				if data.find("plzSent") != -1:
					thread = Thread(target = self.__figthing)
					thread.start()
					break
				else:
					if data.find("data") != -1 or data.find("time") != -1:
						thread = Thread(target = self.__figthing)
						thread.start()
						break
				sleep(self.__updateTime)
			except: sleep(self.__updateTime)

	def __figthing(self):
		self.__execute = True
		self.__linkedserver = True
		threadS = Thread(target = self.__keepSend)
		threadR = Thread(target = self.__keepRecv)
		threadS.start()
		threadR.start()

	def __keepSend(self):
		while self.__execute:
			while len(self.__willSend) != 0:
				text = str(self.__willSend.pop(0))
				self.__socket.send(text.encode('ascii'))
			sleep(self.__updateTime)

	def __keepRecv(self):
		while self.__execute:
			try:
				data = self.__socket.recv(16383).decode('utf8')
				self.__getRecv.append(data)
				gameStatus = data.rfind("time")
				if gameStatus != -1 and len(data) > gameStatus + 7:
					if data[gameStatus+6] == "0":
						self.__execute = False
						self.__linkedserver = False
						self.__socket.close()
						break
					elif data[gameStatus+6] == " ":
						if data[gameStatus+7] == "0":
							self.__execute = False
							self.__linkedserver = False
							self.__socket.close()
							break
				sleep(self.__updateTime)
			except: sleep(self.__updateTime)

	def send(self, text): self.__willSend.append(text)

	def recv(self) -> dict:
		ans = ""
		fin = ""
		right = -1
		ansNum = 0
		time = 1000
		while len(self.__getRecv) != 0:
			text = self.__getRecv.pop(0)
			if text == "": continue

			right = text.find("}")
			if right != -1:
				self.__getRecv.insert(0, text[right+1:])
				ans += text[:right+1]
				try:
					ans = eval(ans)
					for x in ans["data"]:
						if x == '[': ansNum += 1
						elif x == ']': ansNum -= 1
					fin += ans["data"]
					if time > ans["time"]: time = ans["time"]

					if ansNum == 0: return {"data" : eval(fin), "time" : time}

					ans = ""
					right = -1
				except:
					self.__getRecv.insert(0, text[text.find('}')+1:])
					ans = ""
					right = -1
			else:
				ans += text
				right = -1
		return ""

	def shutdown(self):
		self.__socket.close()
		self.__execut = False
		self.__linkedserver = False
		
	@property
	def done(self) -> bool: return self.__execute

	@property
	def gameStart(self) -> bool: return self.__linkedserver

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
	msg = [[[0 for i in range(10)] for j in range(20)] for k in range(7)]
	net = PGinternet(updateTime = 1, IP = "192.168.88.128", host = 9487)
	net.link()

	while net.done:
		while net.gameStart:
			net.send(msg)
			data = net.recv()
			print(data["data"], data["time"])
			sleep(1)
