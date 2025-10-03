def is_solved(board):
    # 2 diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return 1 if board[0][0] == 1 else 2
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return 1 if board[0][2] == 1 else 2
    # 3 vertical
    for index in range(3):
        if board[0][index] == board[1][index] == board[2][index] and board[0][index] != 0:
            return 1 if board[0][index] == 1 else 2
    # 3 horizontal
    for row in board:
        if row[0] == row[1] == row [2] and row[0] != 0:
            return 1 if row[0] == 1 else 2
    # checking for 0 (not complete game)
    for row in board:
        if row[0] == 0 or row[1] == 0 or row [2] == 0:
            return -1
    # returning 0 bcs of tie
    return 0