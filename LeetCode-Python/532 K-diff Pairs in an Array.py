"""
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff
pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
    Input: [3, 1, 4, 1, 5], k = 2
    Output: 2
    Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
    Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:
    Input:[1, 2, 3, 4, 5], k = 1
    Output: 4
    Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:
    Input: [1, 3, 1, 5, 4], k = 0
    Output: 1
    Explanation: There is one 0-diff pair in the array, (1, 1).

Note:
    The pairs (i, j) and (j, i) count as the same pair.
    The length of the array won't exceed 10,000.
    All the integers in the given input belong to the range: [-1e7, 1e7].
"""

# Time Limit Exceeded
"""
def findPairs(nums, k):
    # sort the nums
    nums = sorted(nums)
    print(nums)
    num_of_pairs = 0
    pairs = set()
    # iterate the nums to find the unique k-diff pairs
    for i in range(0, len(nums)):
        if nums[i] + k in nums[i + 1:]:
            if (nums[i], nums[i] + k) not in pairs:
                num_of_pairs += 1
                pairs.add((nums[i], nums[i] + k))
        # delete the small from the nums list
    return num_of_pairs
"""
# Time Limit Exceeded
def findPairs(nums, k):
    # sort the nums
    nums = sorted(nums)
    print(nums)
    num_of_pairs = 0
    # iterate the nums to find the unique k-diff pairs
    index = 0
    l = len(nums)
    last = None
    while index < l - 1:
        num = nums[index]
        if num != last:
            for i in range(index + 1, l):
                if num + k < nums[i]:
                    break
                elif num + k == nums[i]:
                    print((nums[index], nums[i]))
                    num_of_pairs += 1
                    break
        last = nums[index]
        del nums[index]
        l -= 1
    return num_of_pairs

def findPairs2(nums, k):
    nums = sorted(nums)
    pairs = set()
    start_index = 0
    index = 1
    while index < len(nums):
        last = nums[start_index]
        if nums[index] <= last + k:
            if nums[index] == last:
                start_index += 1

            if nums[index] == last + k:
                pair = (last, last + k)
                pairs.add(pair)
        else:
            while nums[index] >= nums[start_index] + k and start_index < index:
                start_index += 1
                if start_index != index:
                    last = nums[start_index]
                    if nums[index] == last + k:
                        pair = (last, last + k)
                        pairs.add(pair)
        index += 1
    return len(pairs)

input1 = [3, 1, 4, 1, 5]
k1 = 2
print(findPairs2(input1, k1))

input2 = [1, 2, 3, 4, 5]
k2 = 1
print(findPairs2(input2, k2))

input3 = [1, 3, 1, 5, 4]
k3 = 0
print(findPairs2(input3, k3))

input4 = [1, 3, 1, 5, 4]
k4 = 0
print(findPairs2(input4, k4))

input5 = [1, 1, 1, 1, 1]
k5 = 0
print(findPairs2(input5, k5))

input6 = reversed([0,1,2,3,4,5,6,7,8])
k6 = 1
print(findPairs2(input6, k6))

input7 = [1, 2, 3, 4, 5]
k7 = 0
print(findPairs2(input7, k7))

input8 = [1,1,1,2,2]
k8 = 0
print(findPairs2(input8, k8))

input9 = [6,7,3,6,4,6,3,5,6,9]
k9 = 4
print(findPairs2(input9, k9))

input10 = [1,3,1,5,4]
k10 = 0
print(findPairs2(input10, k10))
