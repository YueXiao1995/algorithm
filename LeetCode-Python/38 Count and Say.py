"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:
    Input: 1
    Output: "1"

Example 2:
    Input: 4
    Output: "1211"
"""

def countAndSay(n: int) -> str:
    # init the sequence
    sequence = "1"
    # iterate n-1 times
    while n - 1 > 0:
        # use a string to record the new sequence
        new_sequence = ""
        # record the last num
        last_num = None
        # the length of consecutive sequence of the same num
        num_of_same = 0
        # iterate over the sequence string
        for i in range(len(sequence)):
            # in first iterate, init the last num
            if last_num == None:
                last_num = sequence[i]
                num_of_same += 1
            else:
                if last_num == sequence[i]:
                    num_of_same += 1
                else:
                    # expend the new sequence
                    new_sequence += str(num_of_same) + last_num
                    # update the last num and init the length of same num string
                    num_of_same = 1
                    last_num = sequence[i]
        # append the length and num of the last sub sequence to the new sequence
        new_sequence += str(num_of_same) + last_num
        # update the sequence
        sequence = new_sequence
        n -= 1
    return sequence

input1 = 1
input2 = 4
print(countAndSay(input1))
