"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.


Example:
    Input:
    [4,3,2,7,8,2,3,1]

    Output:
    [5,6]
"""
"""
def findDisappearedNumbers(nums):
    n = len(nums)
    missed_nums = list(range(1, n + 1))
    duplicated_nums = list()

    for num in nums:
        try:
            missed_nums.remove(num)
        except:
            continue
    return missed_nums
"""
def findDisappearedNumbers(nums):
    n = len(nums)
    missed_nums = set(list(range(1, n + 1))) - set(nums)
    return list(missed_nums)
input = [4,3,2,7,8,2,3,1]

# set is the fastest way to find a value, far quicker than iterating a list

print(findDisappearedNumbers(input))
