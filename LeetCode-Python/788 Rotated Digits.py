"""
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
    Input: 10
    Output: 4
    Explanation:
    There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
    Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

Note:
    N  will be in range [1, 10000].
"""
# valid numbers: 2, 5, 6, 9, 12, 15, 16, 19, 20....
# 1, 0, 8
# 2, 5, 6, 9
def rotatedDigits(N: int) -> int:
    # for a good number, all of its digit should in set i and at least one digit in set 2
    digits_1 = {1, 0, 8, 2, 5, 6, 9}
    digits_2 = {2, 5, 6, 9}

    amount_of_good_nums = 0
    i = 1
    # iterate over the numbers from 1 to N
    while i <= N:
        # assume the number is not a good number at first
        is_good_number = False
        # iterate over its digit
        for char in str(i):
            # check if the digit is in set 1
            if int(char) in digits_1:
                # check if the digit is in set 2
                if int(char) in digits_2:
                    is_good_number = True
            else:
                # it find a digit that not in set 2, break the loop
                is_good_number = False
                break
        # update the number of good numbers
        if is_good_number:
            amount_of_good_nums += 1
        i += 1

    return amount_of_good_nums

input1 = 857

print(rotatedDigits(input1))
