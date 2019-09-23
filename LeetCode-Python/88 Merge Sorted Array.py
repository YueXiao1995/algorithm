"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:
    Input:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],       n = 3
    Output: [1,2,2,3,5,6]
"""

"""
def merge(nums1, m, nums2, n):
    newlist = list()
    index1 = 0
    index2 = 0
    while(index1 < m or index2 < n):
        print(index1)
        print(index2)
        print(newlist)
        if nums1[index1] <= nums2[index2] and nums1[index1] != 0:
            newlist.append(nums1[index1])
            index1 += 1
        else:
            newlist.append(nums2[index2])
            index2 += 1
    return newlist
"""
def merge(nums1, m, nums2, n):
    index1 = 0
    index2 = 0
    if n != 0:
        while(index2 < n):
            if index1 < m + index2:
                if nums1[index1] < nums2[index2]:
                    index1 += 1
                else:
                    pre = nums1[index1]
                    for i in range(index1 + 1, m + n):
                        temp = nums1[i]
                        nums1[i] = pre
                        pre = temp
                    nums1[index1] = nums2[index2]
                    index2 += 1
            else:
                if nums1[index1] < nums2[index2] and nums1[index1] != 0:
                    index1 += 1
                else:
                    pre = nums1[index1]
                    for i in range(index1+1, m+n):
                        temp = nums1[i]
                        nums1[i] = pre
                        pre = temp
                    nums1[index1] = nums2[index2]
                    index2 += 1
        return nums1
    else:
        return nums1

nums1 = [-1,3,0,0,0,0,0]
m = 2
nums2 = [0,0,1,2,3]
n = 5
print(merge(nums1, m, nums2, n))

