"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
    Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
    Output: [-1,3,-1]
    Explanation:
        For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
        For number 1 in the first array, the next greater number for it in the second array is 3.
        For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2:
    Input: nums1 = [2,4], nums2 = [1,2,3,4].
    Output: [3,-1]
    Explanation:
        For number 2 in the first array, the next greater number for it in the second array is 3.
        For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

Note:
    All elements in nums1 and nums2 are unique.
    The length of both nums1 and nums2 would not exceed 1000.
"""

def nextGreaterElement(nums1, nums2):
    # store the num in nums1 into a dict as the key, the value will be the next greater number
    next_great_numbers = dict()
    for num in nums1:
        next_great_numbers[num] = None

    # use a stack to store the num in nums2, from the last one to the first one
    stack = list()
    for num in reversed(nums2):
        # check if the num is also in nums1
        if num in nums1:
            # init the next great number to -1
            next_great_number = -1
            # try to find the next great number
            for i in reversed(range(len(stack))):
                if stack[i] > num:
                    next_great_number = stack[i]
                    break
            # store the next great number of the target num
            next_great_numbers[num] = next_great_number
        # push the num into the stack
        stack.append(num)

    # sort the next great numbers in the order of its key's order in the nums1
    result = list()
    for num in nums1:
        result.append(next_great_numbers[num])
    
    return result

nums1 = [4,1,2]
nums2 = [1,3,4,2]

nums3 = [2,4]
nums4 = [1,2,3,4]

print(nextGreaterElement(nums3, nums4))
