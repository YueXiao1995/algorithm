"""
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.

Example 1:
    Input: 2
    Output: true
    Explanation: Alice chooses 1, and Bob has no more moves.

Example 2:
    Input: 3
    Output: false
    Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.

Note:
    1 <= N <= 1000
"""

def divisorGame(N):
    is_Alice_Turn = True
    while N > 1:
        x = None
        for i in reversed(range(1, N)):
            if N % i == 0:
                x = i
                break
        N -= x
        is_Alice_Turn = not is_Alice_Turn

    if is_Alice_Turn:
        return False
    else:
        return True

input1 = 2
input2 = 3
input3 = 4
print(divisorGame(input3))
