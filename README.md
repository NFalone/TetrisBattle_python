# TetrisBattle\_python
Game TetrisBattle from Facebook using python tkinter.

## Server

Tetris Battle Server with NodeJS-17
- Timer
- Match
- Tell client game status now

### How to use

Text Encoding: UTF-8.  
This docker container gonna listen at:
- (Docker) port 9487
- (Other) port 80

If you try connectinig this server.  
There have two examples, which Python and JavaScript.  
You Can follow the **how\_to\_connect.py** or **how\_to\_connect.js**.

#### start this server

##### Docker(Recommend)

```sh
cd server
docker-compose up -d
```

##### Npm

```sh
cd server/web
npm run test
```

##### NodeJS

```sh
cd server/web
node ./netWebSever.js 
```

#### start the "How To Connect" file

##### Docker

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

##### compiler

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
