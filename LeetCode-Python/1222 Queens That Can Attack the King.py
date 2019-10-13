"""
On an 8x8 chessboard, there can be multiple Black Queens and one White King.

Given an array of integer coordinates queens that represents the positions of the Black Queens, and a pair of coordinates king that represent the position of the White King, return the coordinates of all the queens (in any order) that can attack the King.



Example 1:



Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
Output: [[0,1],[1,0],[3,3]]
Explanation:
The queen at [0,1] can attack the king cause they're in the same row.
The queen at [1,0] can attack the king cause they're in the same column.
The queen at [3,3] can attack the king cause they're in the same diagnal.
The queen at [0,4] can't attack the king cause it's blocked by the queen at [0,1].
The queen at [4,0] can't attack the king cause it's blocked by the queen at [1,0].
The queen at [2,4] can't attack the king cause it's not in the same row/column/diagnal as the king.
Example 2:



Input: queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
Output: [[2,2],[3,4],[4,4]]
Example 3:



Input: queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]
Output: [[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]


Constraints:

1 <= queens.length <= 63
queens[0].length == 2
0 <= queens[i][j] < 8
king.length == 2
0 <= king[0], king[1] < 8
At most one piece is allowed in a cell.
"""

def queensAttacktheKing(queens, king):
    # use 8 list to store the queens in the 8 different directions of the king
    left = list()
    right = list()
    top = list()
    bottom = list()
    top_left = list()
    top_right = list()
    bottom_left = list()
    bottom_right = list()

    # iterate over the list of queens, and find the queens in these 8 directions which can directly attack the king
    queens_can_attack = list()
    for queen in queens:
        if queen[0] == king[0]:
            if queen[1] < king[1]:
                left.append(queen)
            else:
                right.append(queen)
        elif queen[1] == king[1]:
            if queen[0] > king[0]:
                bottom.append(queen)
            else:
                top.append(queen)
        elif abs(queen[1] - king[1]) == abs(queen[0] - king[0]):
            if queen[0] < king[0] and queen[1] < king[1]:
                top_left.append(queen)
            elif queen[0] < king[0] and queen[1] > king[1]:
                top_right.append(queen)
            elif queen[0] > king[0] and queen[1] < king[1]:
                bottom_left.append(queen)
            elif queen[0] > king[0] and queen[1] > king[1]:
                bottom_right.append(queen)
    # if the list is not empty, sort the list by the distance to the king, store the first one into the result list
    if len(top) != 0:
        queens_can_attack.append(sorted(top, key=lambda l: abs(l[0] - king[0]))[0])
    if len(bottom) != 0:
        queens_can_attack.append(sorted(bottom, key=lambda l: abs(l[0] - king[0]))[0])
    if len(left) != 0:
        queens_can_attack.append(sorted(left, key=lambda l: abs(l[1] - king[1]))[0])
    if len(right) != 0:
        queens_can_attack.append(sorted(right, key=lambda l: abs(l[1] - king[1]))[0])
    if len(top_left) != 0:
        queens_can_attack.append(sorted(top_left, key=lambda l: abs(l[1] - king[1]))[0])
    if len(top_right) != 0:
        queens_can_attack.append(sorted(top_right, key=lambda l: abs(l[1] - king[1]))[0])
    if len(bottom_left) != 0:
        queens_can_attack.append(sorted(bottom_left, key=lambda l: abs(l[1] - king[1]))[0])
    if len(bottom_right) != 0:
        queens_can_attack.append(sorted(bottom_right, key=lambda l: abs(l[1] - king[1]))[0])

    return queens_can_attack


queens1 = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]
king1 = [0,0]

queens2 = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]]
king2 = [3,3]

queens3 = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]]
king3 = [3,4]

print(queensAttacktheKing(queens3, king3))
