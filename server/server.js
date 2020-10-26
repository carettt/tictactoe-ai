const express = require('express');
const socket = require('socket.io');
const app = express();
const port = process.env.PORT || 3000;

let server = app.listen(port, () => {
    console.log('Socket server running...');
});

app.use(express.static('server/public'), (res, req) => {
    req.header('Access-Control-Allow-Origin: http://localhost:3000/socket.io/');
});

let io = socket(server);

io.sockets.on('connection', (socket) => {
    console.log('New connection:', socket.id);
    socket.on('board', (data) => {
        socket.broadcast.emit('board', data);
        console.log(data);
    });
});
