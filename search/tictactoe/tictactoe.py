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

    # Counts he number of Xs and Os on board
    numX = 0
    numO = 0

    for row in range(len(board[0])):
        for square in board[row]:
            if square == X:
                numX += 1
            elif square == O:
                numO += 1

    # Checks if game is over
    # If not and there are more Xs than Os, O will go next because X went first
    if terminal(board):
        return "The Game is Already Over"
    elif numX > numO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return "The Game is Already Over"

    actions = set()

    # Iterates through every square, and if empty adds it to the set of possible moves
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
        raise Exception("Could not find action")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Checks horizontal win condition
    for row in board:
        # result = row.count(row[0]) == len(row)
        if (row.count(X) == len(row)):
            return X
        if (row.count(O) == len(row)):
            return O

    # Checks vertical win condition
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] and board[0][col] == board[2][col]:
            return board[0][col]

    # Checks diagonal win condition
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

    # Game can be continued if there is an open square
    for row in board:
        for cell in row:
            if cell is EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    # X is max
    # O is min
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

        # X always makes the same opening move
        if board == initial_state():
            bestMove = (1, 1)
            return bestMove

        # X is trying to find the move that will maximize their score
        else:
            v = -math.inf
            print("AI is looking for optimal move...")
            for action in actions(board):

                # Checks to see if the action will cause a win condition
                if winner(result(board, action)) != None:
                    return action

                temp = Minimize(result(board, action))
                if temp > v:
                    bestMove = action
                    v = temp

    if player(board) == O:

        # O is trying to find the move that will minimize their score
        v = math.inf
        print("AI is looking for optimal move...")
        for action in actions(board):
            if winner(result(board, action)) != None:
                return action

            temp = Maximize(result(board, action))
            if temp < v:
                bestMove = action
                v = temp

    print("AI found the optimal move :(")
    return bestMove


def Maximize(board):
    v = -math.inf

    if terminal(board):
        return utility(board)

    # Checks every possible action to see if the board can produce a win (+1)
    for action in actions(board):
        v = max(v, Minimize(result(board, action)))

    return v


def Minimize(board):
    v = math.inf

    if terminal(board):
        return utility(board)

    # Checks every possible action to see if the board can produce a win (-1)
    for action in actions(board):
        v = min(v, Maximize(result(board, action)))

    return v
