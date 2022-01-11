const net = require("net");


class bettel
{
	constructor()
	{
		this.agent = [];
		this.waiting = [];
		this.playing = {};
		this.gametime = {};
	}

	match(systemData)
	{
		let tool = new toolbox();
		tool.updateLine(systemData.waiting);
		tool.updateLine(systemData.playing);
		tool.reduceTime(systemData.gametime);

		let player1 = undefined, player2 = undefined;
		if(systemData.waiting.length === 2)
		{
			player1 = 0;
			player2 = 1;
		}
		else if(systemData.waiting.length > 2)
		{
			player1 = Math.floor(Math.random() * systemData.waiting.length);
			player2 = Math.floor(Math.random() * systemData.waiting.length);
		}
		if(player1 !== player2)
		{
			let socket1 = systemData.waiting[player1];
			let socket2 = systemData.waiting[player2];

			if(!!socket1.write && !!socket2.write) 
			{
				socket1.write("linked");
				socket2.write("linked");
			}
			else return;

			systemData.agent.push(socket1);

			socket1.comfirm = socket2.comfirm = false;

			let player1_ID = socket1.remoteAddress + "(" + socket1.remotePort + ")";
			let player2_ID = socket2.remoteAddress + "(" + socket2.remotePort + ")";

			systemData.playing[player1_ID] = socket2;
			systemData.playing[player2_ID] = socket1;

			systemData.gametime[player1_ID] = systemData.gametime[player2_ID] = "wait";

			if(player2 > player1)
			{
				player1 = player1 ^ player2;
				player2 = player1 ^ player2;
				player1 = player1 ^ player2;
			}
			systemData.waiting.splice(player1, 1);
			systemData.waiting.splice(player2, 1);
		}
		tool.sendWaitToClient(systemData.waiting);
	}

	checkComfirm(systemData)
	{
		let ok = [];
		let tool = new toolbox();
		for(let agent of systemData.agent)
		{
			let ID = agent.remoteAddress + "(" + agent.remotePort + ")";

			if(agent["comfirm"] && systemData.playing[ID]["comfirm"])
			{
				if(!!agent.write && !!systemData.playing[ID]) 
				{
					agent.write("plzSent");
					systemData.playing[ID].write("plzSent");

					systemData.gametime[ID] = systemData.gametime[systemData.playing[ID].remoteAddress + "(" + systemData.playing[ID].remotePort + ")"] = 180;

					agent["comfirm"] = systemData.playing[ID]["comfirm"] = false;
					ok.push(agent);
				}
			}
			else continue;
		}
		ok.reverse();
		for(let done of ok) systemData.agent.splice(systemData.agent.indexOf(done), 1);
	}
};

class toolbox
{
	updateLine(Ving)
	{
		let dieSocket = [];

		if(Object.getPrototypeOf(Ving) === Array.prototype)
		{
			for(let check = 0;Ving.length > check;check += 1) if(Ving[check].address().address === undefined) dieSocket.push(check);
			while(dieSocket.length !== 0) Ving.splice(dieSocket.pop(), 1);
		}
		else
		{
			for(let check of Object.keys(Ving)) if(Ving[check].address().address === undefined) dieSocket.push(check);
			dieSocket.reverse();
			while(dieSocket.length !== 0) delete Ving[dieSocket.pop()];
		}
	}

	checkLinked(socket)
	{
		if(socket.address().address === undefined) return false;
		else return true;
	}

	reduceTime(gametime) 
	{
		for(let key of Object.keys(gametime)) if(gametime[key] !== 0 && Number.isInteger(gametime[key])) gametime[key] -= 1;
	}

	sendWaitToClient(waiting) {for(let socket of waiting) socket.write?.("wait");}
};

const server = net.createServer((socket) =>
{
	socket["confirm"] = false;
	gameSystem.waiting.push(socket);

	socket.on("data", (data) =>
	{
		data = data + "";
		let ID = socket.remoteAddress + "(" + socket.remotePort + ")";
		
		switch(gameSystem.gametime[ID])
		{
		case undefined: 
			socket.write("{\"data\":\"done\", \"time\":0}");
			break;
		case "wait": 
			if(/Start/.test(data)) socket["comfirm"] = true;
			break;
		default:
			{
				let gameStatus = Object.create(Object.prototype);
				gameStatus["data"] = data;
				gameStatus["time"] = gameSystem.gametime[ID];
	
				gameSystem.playing[ID].write?.(JSON.stringify(gameStatus));

				if(gameStatus["time"] === 0)
				{
					let ID2 = gameSystem.playing[ID].remoteAddress + "(" + gameSystem.playing[ID].remotePort + ")";
					delete gameSystem.playing[ID];
					delete gameSystem.playing[ID2];
					delete gameSystem.gametime[ID];
					delete gameSystem.gametime[ID2];
				}

				break;
			}
		}

		console.log(ID + ": " + data);
	});

	socket.on("error", (error) => {;});
});

const gameSystem = new bettel();

server.listen(80);
setInterval(gameSystem.match, 1000, gameSystem);
setInterval(gameSystem.checkComfirm, 2000, gameSystem);
