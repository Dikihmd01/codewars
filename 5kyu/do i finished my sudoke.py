def done_or_not(board): #board[i][j]
    for row in range(9):
        if (
            len(set(board[row])) < 9 or
            len(set(board[x][row] for x in range(9))) < 9 or
            len(set(board[row//3*3+x//3][row//3*3+x%3] for x in range(9))) < 9
            ):
                return "Try again!"
    return "Finished!"
