"""
We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.

Example 1:
    Input: [2,7,4,1,8,1]
    Output: 1
    Explanation:
    We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
    we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
    we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
    we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

Note:
    1 <= stones.length <= 30
    1 <= stones[i] <= 1000
"""

def lastStoneWeight(stones):
    while len(stones) > 1:
        stones = sorted(stones)
        if stones[-1] == stones[-2]:
            del stones[-1]
            del stones[-1]
        else:
            stones[-2] = stones[-1] - stones[-2]
            del stones[-1]
    if len(stones) == 0:
        return 0
    else:
        return stones[0]

# this mathed is actually slower
def lastStoneWeight2(stones):
    stones = sorted(stones)
    while len(stones) > 1:
        if stones[-1] == stones[-2]:
            del stones[-1]
            del stones[-1]
        else:
            remain = stones[-1] - stones[-2]
            del stones[-1]
            del stones[-1]
            if len(stones) == 0:
                stones.append(remain)
            else:
                for i in range(len(stones)):
                    if stones[i] > remain:
                        stones.insert(i, remain)
                        break
                    if i == len(stones) - 1:
                        stones.append(remain)
    if len(stones) == 0:
        return 0
    else:
        return stones[0]

input1 = [2,7,4,1,8,1]
input2 = [2, 2]
input3 = [1, 3]
print(lastStoneWeight2(input3))
