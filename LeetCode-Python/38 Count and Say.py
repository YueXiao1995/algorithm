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
    sequence = "1"
    while n - 1 > 0:
        new_sequence = ""
        last_num = None
        num_of_same = 0
        for i in range(len(sequence)):
            if last_num == None:
                last_num = sequence[i]
                num_of_same += 1
            else:
                if last_num == sequence[i]:
                    num_of_same += 1
                else:
                    new_sequence += str(num_of_same) + last_num
                    num_of_same = 1
                    last_num = sequence[i]

        new_sequence += str(num_of_same) + last_num
        sequence = new_sequence
        print(n)
        n -= 1

    return sequence

input1 = 1
input2 = 4
print(countAndSay(input1))
