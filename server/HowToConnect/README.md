# start the "How To Connect" file

They both connect the server ten times at the same time.  
When all sockets receive time up, the Python will stop and disconnect, but the JavaScript will keep connecting the server.

## Docker

- JavaScript
```sh
cd server
docker run -ti --rm -v $PWD:/home/node/ -w /home/node node:17 node how_to_connect.js
```

- Python
```sh
cd server
docker run -ti --rm -v $PWD:/home/node/ -w /home/node python:3.10 python3 how_to_connect.py
```

## compiler

- JavaScript
```sh
cd server
node how_to_connect.js
```

- Python
```sh
cd server
python3 how_to_connect.py
```
