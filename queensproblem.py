# Python program to solve the 8-Queens problem using backtracking

N = 8  # Number of queens

def print_board(board):
    """Prints the chessboard"""
    for row in board:
        line = ""
        for cell in row:
            line += "Q " if cell else ". "
        print(line)
    print("\n")

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    # Check this row on left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on left side
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1

    return True

def solve_queens(board, col):
    """Recursive function to solve the 8-queen problem"""
    if col >= N:
        print_board(board)
        return True  # Return True if a solution is found

    res = False
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1  # Place queen
            res = solve_queens(board, col + 1) or res
            board[i][col] = 0  # Backtrack
    return res

# Initialize chessboard
board = [[0 for _ in range(N)] for _ in range(N)]

if not solve_queens(board, 0):
    print("No solution exists")