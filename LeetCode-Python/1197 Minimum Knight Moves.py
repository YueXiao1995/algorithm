"""
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

Example 1:
    Input: x = 2, y = 1
    Output: 1
    Explanation: [0, 0] → [2, 1]

Example 2:
    Input: x = 5, y = 5
    Output: 4
    Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
"""

# Time Limit Exceeded
"""
def minKnightMoves(x, y):
    x = abs(x)
    y = abs(y)
    one_step = {(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)}
    current_position = {(0, 0)}
    previous_fail_position = set()
    num_of_move = 0
    while (x, y) not in current_position:
        possible_position = set()
        for i in range(len(current_position)):
            for j in range(8):
                temp_x = list(current_position)[i][0] + list(one_step)[j][0]
                temp_y = list(current_position)[i][1] + list(one_step)[j][1]
                if temp_x>=0 and temp_y>=0:
                    new_p = (temp_x, temp_y)
                    if new_p not in possible_position and new_p not in previous_fail_position:
                        possible_position.add(new_p)
        for p in current_position:
            previous_fail_position.add(p)

        current_position = possible_position
        print(current_position)
        num_of_move += 1
    return num_of_move
"""
def minKnightMoves(x, y):
    return 0
x1 = 2
y1 = 1
x2 = 5
y2 = 5
x3 = 270
y3 = -21
print(minKnightMoves(x3, y3))
