"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X=0
    O=0
    for row in board:
        for col in row:
            if col == 'X':
                X += 1
            elif col == 'O':
                O += 1
    if X == O:
        return 'X'
    elif X > O:
        return 'O'
    else:
        return 'terminal'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == None:
                moves.append((row,col))
    if len(moves) == 0:
        return 'terminal'
    else:
        return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    tempboard = copy.deepcopy(board)
    if board[action[0]][action[1]] is None:
        move = player(board)
        tempboard[action[0]][action[1]] = move
        return tempboard
    else:
        raise ValueError('Invalid move.')
        return tempboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board [0][1] and board[0][1] == board [0][2] and board[0][0] != None:
        return board[0][0]
    elif board[1][0] == board [1][1] and board[1][1] == board [1][2] and board[1][0] != None:
        return board[1][0]
    elif board[2][0] == board [2][1] and board[2][1] == board [2][2] and board[2][0] != None:
        return board[2][0]
    elif board[0][0] == board [1][0] and board[1][0] == board [2][0] and board[0][0] != None:
        return board[0][0]
    elif board[0][1] == board [1][1] and board[1][1] == board [2][1] and board[0][1] != None:
        return board[0][1]
    elif board[0][2] == board [1][2] and board[1][2] == board [2][2] and board[0][2] != None:
        return board[0][2]
    elif board[0][0] == board [1][1] and board[1][1] == board [2][2] and board[0][0] != None:
        return board[0][0]
    elif board[2][0] == board [1][1] and board[1][1] == board [0][2] and board[2][0] != None:
        return board[2][0]
    else:
        return None 


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    else:
        if actions(board) == 'terminal':
            return True
        else:
            return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    finalresults = winner(board)
    if finalresults == 'X':
        return 1
    elif finalresults == 'O':
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return utility(board)
    if player(board) == 'X':
        if len(actions(board)) >= 8 and board[1][1] == None:
            return (1,1)
        v = -10
        optmove = None
        for action in actions(board):
            tempboard = result(board, action)
            Xresult = utility(tempboard)
            if Xresult == 1:
                return action
            else:
                if terminal(tempboard):
                    return action
                else:
                    minvalue = minfunction(tempboard)
                    if v <= minvalue:
                        v = minvalue
                        optmove = action
        return optmove
    else:
        if len(actions(board)) >= 8 and board[1][1] == None:
            return (1,1)
        v = 10
        optmove = None
        for action in actions(board):
            tempboard = result(board, action)
            Xresult = utility(tempboard)
            if Xresult == -1:
                return action
            else:
                if terminal(tempboard):
                    return action
                else:
                    maxvalue = maxfunction(tempboard)
                    if v >= maxvalue:
                        v = maxvalue
                        optmove = action
        return optmove
                        

def minfunction(board):
    """
    returns the minimum score for a set of action or move
    """
    v = 10
    for action in actions(board):
        tempboard = result(board, action)
        testresult = utility(tempboard)
        if testresult == -1:
            return -1
    return 0
        

def maxfunction(board):
    """
    returns the maximum score for a set of action or move
    """
    v = -10
    for action in actions(board):
        tempboard = result(board, action)
        testresult = utility(tempboard)
        if testresult == 1:
            return 1
    return 0