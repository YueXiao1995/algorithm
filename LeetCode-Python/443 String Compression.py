"""
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

Follow up:
    Could you solve it using only O(1) extra space?

Example 1:
    Input:
    ["a","a","b","b","c","c","c"]

    Output:
    Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

    Explanation:
    "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".

Example 2:
    Input:
    ["a"]

    Output:
    Return 1, and the first 1 characters of the input array should be: ["a"]

    Explanation:
    Nothing is replaced.

Example 3:
    Input:
    ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

    Output:
    Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

    Explanation:
    Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
    Notice each digit has it's own entry in the array.

Note:
    All characters have an ASCII value in [35, 126].
    1 <= len(chars) <= 1000.
"""

def compress(chars):
    l = len(chars)
    i = 0
    while i < l:
        # calculate the repeat times
        repeat_time = 0
        for j in range(i, l):
            if chars[j] == chars[i]:
                repeat_time += 1
            else:
                break
        # check if the repeat time is bigger than 1
        if repeat_time > 1:
            # remove the repeated nums
            for j in range(repeat_time - 1):
                del chars[i]
                l -= 1
            # convert the repeat_time to a list and insert it into the chars
            repeat_time = list(str(repeat_time))
            for j in range(len(repeat_time)):
                chars.insert(i+j+1, repeat_time[j])
            # update the length of the chars and index i
            l += len(repeat_time)
            i += len(repeat_time) + 1
        else:
            i += 1
    return len(chars)

input1 = ["a","a","b","b","c","c","c"]
input2 = ["a"]
input3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

print(compress(input3))
