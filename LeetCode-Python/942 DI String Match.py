"""
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]

Example 1:
    Input: "IDID"
    Output: [0,4,1,3,2]

Example 2:
    Input: "III"
    Output: [0,1,2,3]

Example 3:
    Input: "DDI"
    Output: [3,2,0,1]

Note:
    1 <= S.length <= 10000
    S only contains characters "I" or "D".
"""
def diStringMatch(S):
    l = len(S)
    # generate a list contains the nums form 0 to N
    nums = list(range(l + 1))
    new_permutation = list()
    # iterate the char in S
    for char in S:
        # if char is "I", append the minimum num in nums list to new permutation list
        if char == "I":
            new_permutation.append(nums[0])
            del nums[0]
        else:
            new_permutation.append(nums[-1])
            del nums[-1]
    # append the remain num to the permutation
    new_permutation.append(nums[0])
    return new_permutation

input1 = "IDID"
input2 = "III"
input3 = "DDI"

print(diStringMatch(input1))
