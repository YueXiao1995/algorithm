"""
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.

"""
def numRookCaptures(board):
    height = len(board)
    weidth = len(board[0])
    R = None
    for i in range(height):
        for j in range(weidth):
            if board[i][j] == 'R':
                R = [i, j]
                break
    print(R)
    p_list = list()

    for i in range(height):
        if board[i][R[1]] == 'p':
            p_list.append([i, R[1]])
    for i in range(weidth):
        if board[R[0]][i] == 'p':
            p_list.append([R[0], i])

    print(p_list)

    num_rock_captures = 0

    for p in p_list:
        is_clean = True
        if p[0] == R[0]:
            if p[1] > R[1]:
                start = R[1]
                end = p[1]
            else:
                start = p[1]
                end = R[1]

            for i in range(start + 1, end):
                if board[p[0]][i] != '.':
                    is_clean = False
                    break
        else:
            if p[0] > R[0]:
                start = R[0]
                end = p[0]
            else:
                start = p[0]
                end = R[0]
            for i in range(start + 1, end):
                if board[i][p[1]] != '.':
                    is_clean = False
                    break
        if is_clean:
            num_rock_captures += 1

    return num_rock_captures


input = [[".",".",".",".",".",".",".","."],
         [".",".",".","p",".",".",".","."],
         [".",".",".","p",".",".",".","."],
         ["p","p",".","R",".","p","B","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".","B",".",".",".","."],
         [".",".",".","p",".",".",".","."],
         [".",".",".",".",".",".",".","."]]

print(numRookCaptures(input))
