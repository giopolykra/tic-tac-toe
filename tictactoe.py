"""
Tic Tac Toe Player
"""

import math
import copy

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
    The following works even in the case where no move has been 
    done yet because then "X" play first (xx==oo thus it is "X"'s turn)
    """
    xx = sum([board[i].count("X") for i in range(len(board))])
    oo = sum([board[i].count("O") for i in range(len(board))])
    if xx > oo:
        return "O"
    else:
        return "X"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_ = []
    for row_index, row in enumerate(board):
        for column_index, item in enumerate(row):
            if item == EMPTY:
                actions_.append((row_index, column_index))
    return actions_
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # while action!= None:
    i, j = action
    if i not in [0, 1, 2] or j not in [0, 1, 2]:
        raise InvalidActionError(
            action, board, 'Result function given an invalid board position for action: ')
    if board[i][j] != None:
        raise InvalidActionError(
            action, board, 'Result function tried to perform invalid action on occupaied tile: ')
        # raise Exception

    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    A = None
    for s in ["X", "O"]:
        # check rows
        for row in board:
            if row.count(s) == 3:
                return s
        # check columns
        for i in range(3):
            column = [board[k][i] for k in range(3)]
            if column.count(s) == 3:
                return s
        # check diagonals
        if [board[i][i] for i in range(3)] == 3*[s]:
            return s
        if [board[i][2-i] for i in range(3)] == 3*[s]:
            return s
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) != None) or (actions(board) == []):
        return True
    else:
        return False
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    if winner(board) == "O":
        return -1
    else:
        return 0
    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    def max_value(board):
        best_move = ()
        if terminal(board):
            return utility(board), best_move
        else:
            v = -10
            best_move = ()
            for action in actions(board):
                min_v = min_value(result(board, action))[0]
                if v < min_v:
                    v = min_v
                    best_move = action
            return v, best_move

    def min_value(board):
        best_move = ()
        if terminal(board):
            return utility(board), best_move
        else:
            v = 10
            for action in actions(board):
                max_v = max_value(result(board, action))[0]
                if v > max_v:
                    v = max_v
                    best_move = action
            return v, best_move

    current_player = player(board)

    if current_player == "X":
        return max_value(board)[1]
    else:
        return min_value(board)[1]

    # raise NotImplementedError