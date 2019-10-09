"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:
    int k = 3;
    int[] arr = [4,5,8,2];
    KthLargest kthLargest = new KthLargest(3, arr);
    kthLargest.add(3);   // returns 4
    kthLargest.add(5);   // returns 5
    kthLargest.add(10);  // returns 5
    kthLargest.add(9);   // returns 8
    kthLargest.add(4);   // returns 8

Note:
    You may assume that nums' length ≥ k-1 and k ≥ 1.
"""

# Time Limit Exceeded
class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.nums = list()
        for num in reversed(sorted(nums)):
            self.nums.append(num)
        """
        :type k: int
        :type nums: List[int]
        """

    def add(self, val):
        print(self.nums)
        if len(self.nums) == 0:
            self.nums.insert(0, val)
            if self.k == 1:
                return self.nums[self.k - 1]
            else:
                return None
        else:
            for i in range(len(self.nums)):
                if self.nums[i] < val:
                    self.nums.insert(i, val)
                    if len(self.nums) >= self.k:
                        return self.nums[self.k - 1]
            self.nums.append(val)
            if len(self.nums) >= self.k:
                return self.nums[self.k - 1]

        """
        :type val: int
        :rtype: int
        """

k = 3
arr = [4, 5, 8, 2]
kthLargest = KthLargest(k, arr)
print(kthLargest.add(3))   # returns 4
print(kthLargest.add(5))   # returns 5
print(kthLargest.add(10))  # returns 5
print(kthLargest.add(9))   # returns 8
print(kthLargest.add(4))   # returns 8

