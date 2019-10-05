"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!

Example :
    Input: n = 10, pick = 6
    Output: 6
"""

def guess(num):
    if num > pick:
        return -1
    elif num == pick:
        return 0
    else:
        return 1

def guessNumber(n):
    start = 1
    end = n
    while start < end:
        middle = (start + end) // 2
        if guess(middle) == -1:
            end = middle - 1
        elif guess(middle) == 0:
            return middle
        else:
            start = middle + 1
    return start

n = 10
pick = 6

print(guessNumber(10))
