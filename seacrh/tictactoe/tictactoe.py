"""
Tic Tac Toe Player
"""
import copy
import math

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
    numX = 0
    numO = 0

    for row in range(len(board[0])):
        for square in board[row]:
            if square == X:
                numX += 1
            elif square == 0:
                numO += 1

    if terminal(board):
        return "The Game is Already Over"
    elif numX > numO:
        return O
    elif numO == numX:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return "The Game is Already Over"

    actions = set()

    for i in range(len(board[0])):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = copy.deepcopy(board)

    if action in actions(board):
        x = action[0]
        y = action[1]

        newBoard[x][y] = player(board)
        return newBoard

    else:
        raise NameError("Could not find action")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check horizontal
    for row in board:
        # result = row.count(row[0]) == len(row)
        if (row.count(X) == len(row)):
            return X
        if (row.count(O) == len(row)):
            return O

    # Check vertical
    for col in range(len(board[0])):
        if board[col][0] == board[col][1] and board[col][0] == board[col][2]:
            return board[col][0]

    # Check diagonal
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    for row in board:
        for cell in row:
            if cell is EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    bestMove = None

    if player(board) == X:
        if board == initial_state():
            bestMove = (1, 1)
            return bestMove
        else:
            prevMax = -math.inf
            for action in actions(board):
                max = Minimize(result(board, action))
                if max > prevMax:
                    bestMove = action
                    prevMax = max

    if player(board) == O:
        prevMin = math.inf
        for action in actions(board):
            min = Minimize(result(board, action))
            if min > prevMin:
                bestMove = action
                prevMin = min

    return bestMove


def Maximize(board):
    v = -math.inf

    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = max(v, Minimize(result(board, action)))

    return v


def Minimize(board):
    v = math.inf

    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = min(v, Maximize(result(board, action)))

    return v
