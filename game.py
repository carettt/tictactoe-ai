import network

board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]
win = False

def displayBoard():
    print(board[0], '|', board[1], '|', board[2])
    print('----------')
    print(board[3], '|', board[4], '|', board[5])
    print('----------')
    print(board[6], '|', board[7], '|', board[8])

def convertToInputs():
    inputs = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    for i in range(0, len(board)):
        if board[i] == 'x':
            inputs[i] = 1.0
        elif board[i] == 'o':
            inputs[i] = -1.0
        else:
            inputs[i] = 0.0
    return inputs


displayBoard()
neuralNetwork = network.Network()

while win == False:
    try:
        print('Player 1 pick a spot on the board: ')
        spot = int(input())
        if (board[spot] != 'x' and board[spot] != 'o'):
            board[spot] = 'x'
        else:
            print('\nSpot is taken\n')
    except Exception as e:
        print('Wrong input')
    displayBoard()
    try:
        print('Player 2 pick a spot on the board: ')
        spot = int(input())
        if (board[spot] != 'x' and board[spot] != 'o'):
            board[spot] = 'o'
        else:
            print('\nSpot is taken\n')
    except Exception as e:
        print('Wrong input')
    displayBoard()
    inputs = convertToInputs()
    neuralNetwork.think(inputs)
    output = neuralNetwork.output()
    if output[0]:
        print(output[1], 'won!')
        win = True
