"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
    Input: [1, 2, 2, 3, 1]
    Output: 2
    Explanation:
        The input array has a degree of 2 because both elements 1 and 2 appear twice.
        Of the subarrays that have the same degree:
        [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
        The shortest length is 2. So return 2.

Example 2:
    Input: [1,2,2,3,1,4,2]
    Output: 6
    Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""

def findShortestSubArray(nums):
    # count the freq of each unique num
    nums_freq = dict()
    for i in range(0, len(nums)):
        if nums[i] not in nums_freq:
            nums_freq[nums[i]] = [i]
        else:
            nums_freq[nums[i]].append(i)

    # find the num which has biggest freq and minimum subarray length
    max_freq = 0
    min_length = None
    for num in nums_freq:
        freq = len(nums_freq[num])
        # if the freq greater than the previous freq
        if freq > max_freq:
            # calculate the biggest diff between the indexs of the num
            temp_min_length = nums_freq[num][-1] - nums_freq[num][0] + 1
            # update the minimum length
            min_length = temp_min_length
            # update the maximum frequency
            max_freq = len(nums_freq[num])

        elif freq == max_freq:
            # calculate the biggest diff between the indexs of the num
            temp_min_length = nums_freq[num][-1] - nums_freq[num][0] + 1

            # for the first num
            if min_length == None:
                min_length = temp_min_length

            # compare the length with the previous minimum length
            elif temp_min_length < min_length:
                # update the minimum length
                min_length = temp_min_length
            # update the maximum frequency
            max_freq = len(nums_freq[num])
    return min_length


input1 = [1, 2, 2, 3, 1]
input2 = [1,2,2,3,1,4,2]

print(findShortestSubArray(input1))
