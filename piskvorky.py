board = str(20* '-')
mark =['o', 'x']
import random


def evaluate (board):
    if 'xxx' in board or 'ooo' in board:
        print('Game ended. Good job.')
        return True
    elif '-' not in board: 
        print('This is a draw.')
        return True
    else:
        print()
        return False

def move (board, mark, position):
    new_board = board #theoretisch überflüssig, weil unten gleich überschrieben
    #tady je treba nadefinoval replace '-' bud 'x' nebo 'o'
    new_board = (board[:position] +mark+ board[position+1:]) 
    #man muss definieren WO diese positin zu ändern ist - in diesem falle im Board
    #+1 damit es ab der nächsten weiter geht mit normalem string, denn sonnst ist es immer um 1 position (die variable gegeben länger)
    #fragen wie man mit replace reingeben kann
    return new_board

def valid_move(board, position):
    if position <=19 :
        if board[position] != '-': #uspr. if position != '-' not in board
            print('This place is taken. \n Please choose a different place.')
            return False
        else:
            return True
    else:
        print('Number has to be between 0-19.\n')
        return False

def user_input():
    position = int(input('Please give me the numeric position, where to put your mark.\n'))
    return (position)

def pc_input():
    position = random.randint(0,19)
    return (position)

choices = False
while choices == False:
    user_play_mark = input('Please choose \'x\' or \'o\'.\n')
    if user_play_mark == 'x':
        print('User_player can start')
        pc_play_mark = 'o'
        mensch_zug = True
        break
    elif user_play_mark == 'o':
        print('PC can start this game')
        pc_play_mark ='x'
        mensch_zug = False
        break

def play_one(board, mensch_zug): 
    is_valid_move = False
    while is_valid_move == False:
        if mensch_zug == True:
            position = user_input()
            mark = user_play_mark
        else:
            position = pc_input()
            mark = pc_play_mark
        is_valid_move = valid_move(board, position)
    board = move(board, mark, position)
    return board


while evaluate(board) ==False:
    board = play_one(board, mensch_zug)
    mensch_zug = not mensch_zug
    print(board)    




