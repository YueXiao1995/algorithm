"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

"""

"""
input = [-2,1,-3,4,-1,2,1,-5,4]
def maxSubArry(nums):
    max_sub_arry = None
    l = len(nums)
    if l == 1:
        return nums[0]

    for i in range(0, l):
        if l - i > 1: # make sure the rest part of list has more than two elements
            temp_sum = 0 # add the first element to temp_sum
            if max_sub_arry == None:
                max_sub_arry = nums[i]

            for j in range(i, l):
                temp_sum += nums[j]
                if temp_sum > max_sub_arry:
                    #print(temp_sum)
                    max_sub_arry = temp_sum

        else:
            if max_sub_arry == None:
                max_sub_arry = nums[i]
            else:
                if nums[i] > max_sub_arry:
                    max_sub_arry = nums[i]
        #print(nums[i])

    return max_sub_arry
"""


def maxSubArry(nums):
    left_sum = nums[0]
    right_sum = 0
    left_index = 0
    index = 0
    l = len(nums)
    for i in range(1, l):
        right_sum += nums[i]
        if right_sum > 0:
            if right_sum > 0:
                index = i
                max_sum = 0
                sum_value = 0
                for j in reversed(range(left_index, i)):
                    sum_value += nums[j]
                    if sum_value > max_sum:
                        max_sum = sum_value
                if max_sum < 0:
                    left_sum = nums[i]
                    left_index = i
                else:
                    left_sum = max_sum + nums[i]

                right_sum = 0
                if nums[i] > left_sum:
                    print(right_sum)
                    left_sum = nums[i]
                    right_sum = 0
                    print("aaa")
        else:
            right_max_sum = nums[i]
            right_sum_value = 0

            # get the biggest right sum
            for k in reversed(range(index, i+1)):
                right_sum_value += nums[k]
                if right_sum_value > right_max_sum:
                     right_max_sum = right_sum_value
            if right_max_sum > left_sum:
                left_sum = right_max_sum
                right_sum = 0
    return left_sum

def maxSubArry2(nums):
    current_max_sum = list()
    current_max_sum.append(nums[0])
    for i in range(1, len(nums)):
        current_max_sum.append(max(current_max_sum[i - 1] + nums[i], nums[i]))
    return max(current_max_sum)
input = [8,-19,5,-4,20]
input2 = [-2,1,-3,4,-1,2,1,-5,4]
input3 = [3,-2,-3,-3,1,3,0]
input4 = [-2,-1]
input5 = [2,-2,-2,0,-2,2,2]
print(maxSubArry(input4))
