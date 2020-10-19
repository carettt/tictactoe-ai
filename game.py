board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]

def displayBoard():
    print(board[0], '|', board[1], '|', board[2])
    print('----------')
    print(board[3], '|', board[4], '|', board[5])
    print('----------')
    print(board[6], '|', board[7], '|', board[8])

displayBoard()

while True:
    try:
        print('Pick a spot on the board: ')
        spot = int(input())
        if (board[spot] != 'x' and board[spot] != 'o'):
            board[spot] = 'x'
        else:
            print('\nSpot is taken\n')
    except Exception as e:
        print('Wrong input')
    displayBoard()
