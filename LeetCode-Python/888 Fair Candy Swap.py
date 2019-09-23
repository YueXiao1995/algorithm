"""
Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy that Alice has, and B[j] is the size of the j-th bar of candy that Bob has.

Since they are friends, they would like to exchange one candy bar each so that after the exchange, they both have the same total amount of candy.  (The total amount of candy a person has is the sum of the sizes of candy bars they have.)

Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange, and ans[1] is the size of the candy bar that Bob must exchange.

If there are multiple answers, you may return any one of them.  It is guaranteed an answer exists.

Example 1:
    Input: A = [1,1], B = [2,2]
    Output: [1,2]

Example 2:
    Input: A = [1,2], B = [2,3]
    Output: [1,2]

Example 3:
    Input: A = [2], B = [1,3]
    Output: [2,3]

Example 4:
    Input: A = [1,2,5], B = [2,4]
    Output: [5,4]

Note:

1 <= A.length <= 10000
1 <= B.length <= 10000
1 <= A[i] <= 100000
1 <= B[i] <= 100000
It is guaranteed that Alice and Bob have different total amounts of candy.
It is guaranteed there exists an answer.
"""


# Time Limit Exceeded
"""
def fairCandySwap(A, B):
    # calculate the difference between the total number of the candy bars Ailce and Bob have
    # calcuate the total amount of the candy Ailce and Bob have
    total_amount_A = 0
    total_amount_B = 0
    for candy in A:
        total_amount_A += candy
    for candy in B:
        total_amount_B += candy
    # calculate the difference
    print(total_amount_A)
    print(total_amount_B)
    diff = total_amount_A - total_amount_B
    print(diff)
    # sort A and B
    A = sorted(A)
    B = sorted(B)
    # find two candy bars which belong to Ailce and Bob respectively, and the difference of their size is half of the difference between the total amount Ailce and Bob have
    for candy_a in A:
        for candy_b in B:
            # check the difference of their size
            candy_diff = candy_a - candy_b
            if candy_diff == diff /2:
                return [candy_a, candy_b]
            elif candy_diff < diff / 2:
                break
"""

def fairCandySwap(A, B):
    # calculate the difference between the total number of the candy bars Ailce and Bob have
    # calcuate the total amount of the candy Ailce and Bob have
    total_amount_A = 0
    total_amount_B = 0
    for candy in A:
        total_amount_A += candy
    for candy in B:
        total_amount_B += candy
    # calculate the difference
    print(total_amount_A)
    print(total_amount_B)
    diff = total_amount_A - total_amount_B
    print(diff)
    # sort A and B
    A = sorted(A)
    B = set(B) # set is much more faster than iterate the list
    print(B)
    # find two candy bars which belong to Ailce and Bob respectively, and the difference of their size is half of the difference between the total amount Ailce and Bob have
    for candy_a in A:
        target_size = int(candy_a - diff / 2)
        if target_size in B:
            return [candy_a, target_size]


A1 = [1,1]
B1 = [2,2]

A2 = [1,2]
B2 = [2,3]

A3 = [2]
B3 = [1,3]

A4 = [1,2,5]
B4 = [2,4]
print(fairCandySwap(A4, B4))
