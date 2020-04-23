"""
Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player A always places "X" characters, while the second player B always places "O" characters.
"X" and "O" characters are always placed into empty squares, never on filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.


Example 1:
    Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
    Output: "A"
    Explanation: "A" wins, he always plays first.
    "X  "    "X  "    "X  "    "X  "    "X  "
    "   " -> "   " -> " X " -> " X " -> " X "
    "   "    "O  "    "O  "    "OO "    "OOX"

Example 2:
    Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
    Output: "B"
    Explanation: "B" wins.
    "X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
    "   " -> " O " -> " O " -> " O " -> "XO " -> "XO "
    "   "    "   "    "   "    "   "    "   "    "O  "

Example 3:
    Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
    Output: "Draw"
    Explanation: The game ends in a draw since there are no moves to make.
    "XXO"
    "OOX"
    "XOX"

Example 4:
    Input: moves = [[0,0],[1,1]]
    Output: "Pending"
    Explanation: The game has not finished yet.
    "X  "
    " O "
    "   "

Constraints:
    1 <= moves.length <= 9
    moves[i].length == 2
    0 <= moves[i][j] <= 2
    There are no repeated elements on moves.
    moves follow the rules of tic tac toe.
"""

def tictactoe(moves):
    # number of moves
    num = len(moves)
    # seperate the moves of player A and B
    moves_A = list()
    moves_B = list()
    for i in range(num):
        if i % 2 == 0:
            moves_A.append(moves[i])
        else:
            moves_B.append(moves[i])
    print(moves_A)
    print(moves_B)

    # check if the player wins the game
    def isWin(moves):
        is_win = False
        # check vertical lines
        for i in range(3):
            for j in range(3):
                if [i, j] not in moves:
                    break
                else:
                    if j == 2:
                        is_win = True
        # check horizontal lines
        for i in range(3):
            for j in range(3):
                if [j, i] not in moves:
                    break
                else:
                    if j == 2:
                        is_win = True
        # check diagonal lines
        digonal1 = [[0, 0], [1, 1], [2, 2]]
        for i in range(3):
            if digonal1[i] not in moves:
                break
            else:
                if i == 2:
                    is_win = True
        digonal2 = [[2, 0], [1, 1], [0, 2]]
        for i in range(3):
            if digonal2[i] not in moves:
                break
            else:
                if i == 2:
                    is_win = True
        return is_win

    # check if A wins
    moves_A = tuple(moves_A)
    if isWin(moves_A):
        return "A"
    # check if B wins
    moves_B = tuple(moves_B)
    if isWin(moves_B):
        return "B"
    # check if the game draw
    if num == 9:
        return "Draw"
    else:
        return "Pending"

moves1 = [[0,0],[2,0],[1,1],[2,1],[2,2]]
moves2 = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
moves3 = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
moves4 = [[0,0],[1,1]]

print(tictactoe(moves4))
