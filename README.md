# TetrisBattle_python
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

#### Docker(Recommend)

```sh
cd server
docker-compose up -d
```

#### npm

```sh
cd server/web
npm run test
```

#### NodeJS

```sh
cd server/web
node ./netWebSever.js 
``` 
