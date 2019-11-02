"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
    Input:  [1,2,3,4]
    Output: [24,12,8,6]
    Note: Please solve it without division and in O(n).

Follow up:
    Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
# Time Limit Exceeded
"""
def productExceptSelf(nums):
    def product(nums):
        p = None
        for i in range(len(nums)):
            if p == None:
                p = nums[i]
            else:
                p *= nums[i]
        return p

    result = []

    for i in range(len(nums)):
        new_nums = list(nums)
        del new_nums[i]
        result.append(product(new_nums))

    return result
"""
def productExceptSelf(nums):
    p1_list = list()
    p1 = 1
    for num in nums:
        p1 *= num
        p1_list.append(p1)

    p2_list = list()
    p2 = 1
    for num in reversed(nums):
        p2 *= num
        p2_list.append(p2)
    p2_list.reverse()

    l = len(nums)
    result = list()
    for i in range(l):
        p = 1
        if i > 0:
            p *= p1_list[i - 1]
        if i < l - 1:
            p *= p2_list[i + 1]
        result.append(p)
    return result

input1 = [1,2,3,4]
print(productExceptSelf(input1))

input2 = [0, 0]
print(productExceptSelf(input2))
