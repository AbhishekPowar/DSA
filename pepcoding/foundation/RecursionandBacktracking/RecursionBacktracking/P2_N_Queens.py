def checkBoard(board, row, col):
    N = len(board) - 1
    # same row check can be skipped
    # if sum(board[row]) > 0:
    # return False

    # same column check
    if sum([board[r][col] for r in range(len(board))]) > 0:
        return False

    # left diagonal /
    x, y = row, col
    while x >= 0 and y >= 0:
        if board[x][y] == 1:
            return False
        x, y = x-1, y-1

    # right diagonal \
    x, y = row, col
    while x >= 0 and y != N+1:
        if board[x][y] == 1:
            return False
        x, y = x-1, y+1
    return True


def solve(board, row, col, temp):
    if checkBoard(board, row, col):
        board[row][col] = 1
        if row == len(board)-1:
            print(temp+f'{row}-{col}, '+'.')
        else:
            for c in range(0, len(board)):
                solve(board, row+1, c, temp+f'{row}-{col}, ')
        board[row][col] = 0
    else:
        return False


if __name__ == "__main__":
    N = int(input())
    
    board = [list((0,)*N) for i in range(N)]
    for c in range(0, N):
        solve(board, 0, c, temp='')
