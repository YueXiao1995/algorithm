"""
Three stones are on a number line at positions a, b, and c.

Each turn, you pick up a stone at an endpoint (ie., either the lowest or highest position stone), and move it to an unoccupied position between those endpoints.  Formally, let's say the stones are currently at positions x, y, z with x < y < z.  You pick up the stone at either position x or position z, and move that stone to an integer position k, with x < k < z and k != y.

The game ends when you cannot make any more moves, ie. the stones are in consecutive positions.

When the game ends, what is the minimum and maximum number of moves that you could have made?  Return the answer as an length 2 array: answer = [minimum_moves, maximum_moves]

Example 1:
    Input: a = 1, b = 2, c = 5
    Output: [1,2]
    Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.

Example 2:
    Input: a = 4, b = 3, c = 2
    Output: [0,0]
    Explanation: We cannot make any moves.

Example 3:
    Input: a = 3, b = 5, c = 1
    Output: [1,2]
    Explanation: Move the stone from 1 to 4; or move the stone from 1 to 2 to 4.

Note:
    1 <= a <= 100
    1 <= b <= 100
    1 <= c <= 100
    a != b, b != c, c != a
"""


def numMovesStones(a, b, c):
    nums = sorted([a, b, c])
    max_moves = nums[-1] - nums[0] -2
    if nums[1] - nums[0] == 1 or nums[2] - nums[1] == 1:
        if nums == [nums[0], nums[0]+ 1, nums[0] + 2]:
            min_moves =  0
        else:
            min_moves = 1
    elif nums[1] - nums[0] == 2 or nums[2] - nums[1] == 2:
        min_moves = 1
    else:
        min_moves = 2
    return [min_moves, max_moves]

a1 = 1
b1 = 2
c1 = 5
print(numMovesStones(a1, b1, c1))

a2= 4
b2 = 3
c2 = 2
print(numMovesStones(a2, b2, c2))

a3 = 3
b3 = 5
c3 = 1
print(numMovesStones(a3, b3, c3))
