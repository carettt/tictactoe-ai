board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]
win = False

def displayBoard():
    #display board neatly on command line
    print(board[0], '|', board[1], '|', board[2])
    print('----------')
    print(board[3], '|', board[4], '|', board[5])
    print('----------')
    print(board[6], '|', board[7], '|', board[8])

def whoWon():
    winStates = [['x', 'x', 'x'], ['o', 'o', 'o']]
    boardStates = [[board[0], board[1], board[2]], [board[3], board[4], board[5]], [board[6], board[7], board[8]], [board[0], board[3], board[6]], [board[1], board[4], board[7]], [board[2], board[5], board[8]], [board[0], board[4], board[8]], [board[2], board[4], board[6]]]
    for i in range(0, 8):
        for j in range(0, 2):
            if winStates[j] == boardStates[i]:
                return [True, winStates[j]]
    return [False, None]
                

displayBoard()

while True:
    while True:
        try:
            print('Player 1 pick a spot on the board: ')
            spot = int(input())
            if (board[spot] != 'x' and board[spot] != 'o'):
                board[spot] = 'x'
                displayBoard()
                break
            else:
                print('\nSpot is taken\n')
        except Exception as e:
            print('Wrong input')
            displayBoard()
    winner = whoWon()
    if winner[0]:
        print(winner[1][0], 'won!')
        break
    while True:
        try:
            print('Player 2 pick a spot on the board: ')
            spot = int(input())
            if (board[spot] != 'x' and board[spot] != 'o'):
                board[spot] = 'o'
                displayBoard()
                break
            else:
                print('\nSpot is taken\n')
        except Exception as e:
            print('Wrong input')
            displayBoard()
    winner = whoWon()
    if winner[0]:
        print(winner[1], 'won!')
        break