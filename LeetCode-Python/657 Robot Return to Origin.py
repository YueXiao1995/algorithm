"""
There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.

Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

Example 1:
    Input: "UD"
    Output: true
    Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.

Example 2:
    Input: "LL"
    Output: false
    Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.
"""

def judgeCircle(moves: str) -> bool:
    # initialize a dict to store the freq of different moves
    move_freq = dict()
    move_freq["U"] = 0
    move_freq["D"] = 0
    move_freq["R"] = 0
    move_freq["L"] = 0
    # count the moves and store the freq into a dict
    for char in moves:
        move_freq[char] += 1
    # check if the numbers of up moves and down moves are equal, if the number of right moves and left moves are equal
    if move_freq["U"] == move_freq["D"] and move_freq["L"] == move_freq["R"]:
        return True
    else:
        return False

input1 = "UD"
input2 = "LL"

print(judgeCircle(input1))
