"""
We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
    Input: [1,3,2,2,5,2,3,7]
    Output: 5
    Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Note:
    The length of the input array will not exceed 20,000.
"""

# this method actually find the longest consecutive harmonious subsequence with maximum difference 2
"""
def findLHS(nums):
    longest_harmonious_subsequence = None
    maximum_length = 0
    temp_harmonious_subsequence = None
    temp_length = 0
    middle_num = None
    last_min_index = None
    last_max_index = None
    last_middel_index = None

    l = len(nums)
    # iterate the nums list
    for i in range(0, l):
        print(longest_harmonious_subsequence)
        if middle_num == None:
            middle_num = nums[i]
            temp_harmonious_subsequence = [nums[i]]
            temp_length = 1
            last_middel_index = i
        else:
            diff = abs(nums[i] - middle_num)
            if diff <= 1:
                temp_harmonious_subsequence.append(nums[i])
                temp_length += 1
                if nums[i - 1] != nums[i]:
                    if nums[i] == middle_num:
                        last_middel_index = i
                    elif nums[i] > middle_num:
                        last_max_index = i
                    else:
                        last_min_index = i
            else:

                if maximum_length < temp_length:
                    longest_harmonious_subsequence = temp_harmonious_subsequence
                    maximum_length = temp_length

                if nums[i] - 1 == middle_num + 1:
                    if last_max_index == None:
                        middle_num = nums[i]
                        temp_harmonious_subsequence = [nums[i]]
                        temp_length = 1
                        last_middel_index = i
                        last_max_index = None
                        last_min_index = None
                    else:
                        if last_max_index > last_middel_index:
                            middle_num = nums[i]
                            temp_harmonious_subsequence = temp_harmonious_subsequence[last_max_index:] + [nums[i]]
                            temp_length = i - last_max_index + 1
                            last_min_index = last_max_index
                            last_middel_index = i
                            last_max_index = None
                        else:
                            middle_num = nums[i]
                            temp_harmonious_subsequence = [nums[i]]
                            temp_length = 1
                            last_middel_index = i
                            last_max_index = None
                            last_min_index = None
                elif nums[i] + 1 == middle_num - 1:
                    if last_min_index == None:
                        middle_num = nums[i]
                        temp_harmonious_subsequence = [nums[i]]
                        temp_length = 1
                        last_middel_index = i
                        last_max_index = None
                        last_min_index = None
                    else:
                        if last_min_index > last_middel_index:
                            middle_num = nums[i]
                            temp_harmonious_subsequence = temp_harmonious_subsequence[last_min_index:] + [nums[i]]
                            temp_length = i - last_min_index + 1
                            last_max_index = last_min_index
                            last_middel_index = i
                            last_min_index = None
                        else:
                            middle_num = nums[i]
                            temp_harmonious_subsequence = [nums[i]]
                            temp_length = 1
                            last_middel_index = i
                            last_max_index = None
                            last_min_index = None
                else:
                    middle_num = nums[i]
                    temp_harmonious_subsequence = [nums[i]]
                    temp_length = 1
                    last_middel_index = i
                    last_max_index = None
                    last_min_index = None
    return longest_harmonious_subsequence
"""

def findLHS(nums):
    # count and record the freq of the nums
    nums_freq = dict()
    for num in nums:
        if num not in nums_freq:
            nums_freq[num] = 1
        else:
            nums_freq[num] += 1

    maximum_length = 0
    # sort the dict by key and iterate it
    for num in nums_freq:
        temp_length = 0
        # check if num + 1 is also in the freq dict
        if num + 1 in nums_freq:
            # temp length equal to the sum of the freqs of num and num + 1
            temp_length += nums_freq[num] + nums_freq[num + 1]
        # update the maximum length
        if temp_length > maximum_length:
            maximum_length = temp_length
    return maximum_length

input1 = [1,3,2,2,5,2,3,7]
print(findLHS(input1))
