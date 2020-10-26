const winStates = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [6, 4, 2]
];
let board = ['', '', '', '', '', '', '', '', ''];
let turn = 'X';

let socket;

function setup() {
    createCanvas(600, 600);
    // frameRate(1);
    // Following code is taken from https://stackoverflow.com/users/607407/tom%c3%a1%c5%a1-zato-reinstate-monica at https://stackoverflow.com/questions/7837456/how-to-compare-arrays-in-javascript
    // Warn if overriding existing method
    if (Array.prototype.equals)
        console.warn(
            "Overriding existing Array.prototype.equals. Possible causes: New API defines the method, there's a framework conflict or you've got double inclusions in your code."
        );
    // attach the .equals method to Array's prototype to call it on any array
    Array.prototype.equals = function (array) {
        // if the other array is a falsy value, return
        if (!array) return false;

        // compare lengths - can save a lot of time
        if (this.length != array.length) return false;

        for (var i = 0, l = this.length; i < l; i++) {
            // Check if we have nested arrays
            if (this[i] instanceof Array && array[i] instanceof Array) {
                // recurse into the nested arrays
                if (!this[i].equals(array[i])) return false;
            } else if (this[i] != array[i]) {
                // Warning - two different object instances will never be equal: {x:20} != {x:20}
                return false;
            }
        }
        return true;
    };
    // Hide method from for-in loops
    Object.defineProperty(Array.prototype, 'equals', { enumerable: false });

    // set socket variable
    socket = io.connect('http://127.0.0.1:3000');

    // recieve data from server (other clients updating)
    socket.on('board', (data) => {
        console.log('test');
        updateTurn(data.spot);
    });
}

function draw() {
    background(220);
    stroke(0);
    displayBoard();
}

function displayBoard() {
    fill(0);
    strokeWeight(15);
    // board divisions
    line(50, 200, 550, 200);
    line(50, 400, 550, 400);
    line(200, 50, 200, 550);
    line(400, 50, 400, 550);
    textSize(50);
    strokeWeight(8);
    // display board values
    text(board[0], 100, 140);
    text(board[1], 285, 140);
    text(board[2], 470, 140);
    text(board[3], 100, 320);
    text(board[4], 285, 320);
    text(board[5], 470, 320);
    text(board[6], 100, 500);
    text(board[7], 285, 500);
    text(board[8], 470, 500);
}

function setX(spot) {
    // set board spot to X if it is available
    if (board[spot] != 'X' && board[spot] != 'O') {
        board[spot] = 'X';
    }
}

function setO(spot) {
    // set board spot to O if it is available
    if (board[spot] != 'X' && board[spot] != 'O') {
        board[spot] = 'O';
    }
}

function whoWon() {
    for (let i = 0; i < 8; i++) {
        win = new Array(3);
        // set win to one of the win states
        for (let j = 0; j < 3; j++) {
            win[j] = board[winStates[i][j]];
        }
        // check if board is in win state
        if (win.equals(['X', 'X', 'X'])) {
            return 'X';
        } else if (win.equals(['O', 'O', 'O'])) {
            return 'O';
        }
    }
    return null;
}

function updateTurn(spot) {
    //update spots based on turn
    if (turn == 'X') {
        setX(spot);
        turn = 'O';
    } else if (turn == 'O') {
        setO(spot);
        turn = 'X';
    }

    //check winner
    let winner = whoWon();
    if (winner != null) {
        console.log(winner, 'won!');
        clearBoard();
    }
}

function clearBoard() {
    board = ['', '', '', '', '', '', '', '', ''];
}

function mouseClicked() {
    fill(0);
    circle(mouseX, mouseY, 5);
    console.log(mouseX, mouseY);
    let spot;
    // update certain board spots depending on mouseX and mouseY
    if (mouseX > 50 && mouseX < 200 && mouseY > 50 && mouseY < 200) {
        spot = 0;
        updateTurn(spot);
    } else if (mouseX > 200 && mouseX < 400 && mouseY > 50 && mouseY < 200) {
        spot = 1;
        updateTurn(spot);
    } else if (mouseX > 400 && mouseX < 550 && mouseY > 50 && mouseY < 200) {
        spot = 2;
        updateTurn(spot);
    } else if (mouseX > 50 && mouseX < 200 && mouseY > 200 && mouseY < 400) {
        spot = 3;
        updateTurn(spot);
    } else if (mouseX > 200 && mouseX < 400 && mouseY > 200 && mouseY < 400) {
        spot = 4;
        updateTurn(spot);
    } else if (mouseX > 400 && mouseX < 550 && mouseY > 200 && mouseY < 400) {
        spot = 5;
        updateTurn(spot);
    } else if (mouseX > 50 && mouseX < 200 && mouseY > 400 && mouseY < 550) {
        spot = 6;
        updateTurn(spot);
    } else if (mouseX > 200 && mouseX < 400 && mouseY > 400 && mouseY < 550) {
        spot = 7;
        updateTurn(spot);
    } else if (mouseX > 400 && mouseX < 550 && mouseY > 400 && mouseY < 550) {
        spot = 8;
        updateTurn(spot);
    }

    // send data to server via websocket
    let data = {
        spot: spot
    };
    socket.emit('board', data);

    fill(255);
}
