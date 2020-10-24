const express = require('express');
const socket = require('socket.io');
const app = express();

let server = app.listen(3000, () => {
    console.log('Socket server running...');
});

app.use(express.static('public'));

// let io = socket(server);

// io.sockets.on('connection', (socket) => console.log(socket));
