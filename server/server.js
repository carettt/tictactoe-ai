const express = require('express');
const socket = require('socket.io');
const app = express();

let server = app.listen(process.env.PORT || 3000, (req, res) => {
    res.header(
        "Content-Security-Policy: default-src *; style-src 'self' 'unsafe-inline'; font-src 'self' data:; script-src 'self' 'unsafe-inline' 'unsafe-eval' stackexchange.com"
    );
    console.log('Socket server running...');
});

app.use(express.static('public'));

let io = socket(server);

io.sockets.on('connection', (socket) => {
    console.log('New connection:', socket.id);
    socket.on('board', (data) => {
        socket.broadcast.emit('board', data);
        console.log(data);
    });
});
