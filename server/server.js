const express = require('express');
const socket = require('socket.io');
const app = express();

let server = app.listen(3000, () => {
    console.log('Socket server running...');
});

app.use(express.static('server/public'));

let io = socket(server);

io.sockets.on('connection', (socket) => {
    console.log('New connection:', socket.id);
    socket.on('board', (data) => {
        socket.broadcast.emit('board', data);
        console.log(data);
    });
});
