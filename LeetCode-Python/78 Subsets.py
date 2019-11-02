"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

def subsets(nums):
    # init the subsets list
    subsets_list = list()
    subsets_list.append([])

    # generate new subsets
    for num in nums:
        new_subsets = list()
        for subset in subsets_list:
            new_subsets.append(subset + [num])
        subsets_list.extend(new_subsets)

    return subsets_list
nums1 = [1, 2, 3]
print(subsets(nums1))
