const net = require("net");


let linked = []
let range = [...Array(10).keys()]

for(let x of range) linked.push("");
for(let x of range) linked[x] = net.connect(9487, "192.168.88.128");

for(let x of range)
{
	linked[x].on("data", (data) =>
	{
		data = data + "";
		if(/linked/.test(data)) 
		{
			console.log(`player${x+1} Link start!`);
			linked[x].write("Start");
		}
		if(/plzSent/.test(data)) 
		{
			console.log(`player${x+1} game start!`);
			linked[x]["reSent"] = setInterval((text) => {linked[x].write(text)}, 1000, `[[[${x}, ${x}, ${x}, ${x}, ${x}]]]`)
		}
		else console.log(`player${x+1} is ` + data);
	});

	linked[x].on("end", ()=>{if(linked[x]["reSent"]) clearInterval(linked[x]["reSent"]);});
}
