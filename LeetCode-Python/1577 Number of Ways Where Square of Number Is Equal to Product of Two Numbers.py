"""
Given two arrays of integers nums1 and nums2, return the number of triplets formed (type 1 and type 2) under the following rules:

Type 1: Triplet (i, j, k) if nums1[i]2 == nums2[j] * nums2[k] where 0 <= i < nums1.length and 0 <= j < k < nums2.length.
Type 2: Triplet (i, j, k) if nums2[i]2 == nums1[j] * nums1[k] where 0 <= i < nums2.length and 0 <= j < k < nums1.length.

Example 1:
    Input: nums1 = [7,4], nums2 = [5,2,8,9]
    Output: 1
    Explanation: Type 1: (1,1,2), nums1[1]^2 = nums2[1] * nums2[2]. (4^2 = 2 * 8).

Example 2:
    Input: nums1 = [1,1], nums2 = [1,1,1]
    Output: 9
    Explanation: All Triplets are valid, because 1^2 = 1 * 1.
    Type 1: (0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2).  nums1[i]^2 = nums2[j] * nums2[k].
    Type 2: (0,0,1), (1,0,1), (2,0,1). nums2[i]^2 = nums1[j] * nums1[k].

Example 3:
    Input: nums1 = [7,7,8,3], nums2 = [1,2,9,7]
    Output: 2
    Explanation: There are 2 valid triplets.
    Type 1: (3,0,2).  nums1[3]^2 = nums2[0] * nums2[2].
    Type 2: (3,0,1).  nums2[3]^2 = nums1[0] * nums1[1].

Example 4:
    Input: nums1 = [4,7,9,11,23], nums2 = [3,5,1024,12,18]
    Output: 0
    Explanation: There are no valid triplets.


Constraints:
    1 <= nums1.length, nums2.length <= 1000
    1 <= nums1[i], nums2[i] <= 10^5
"""

import math

def numTriplets(nums1, nums2):
    type1_valid_triplets = set()
    type2_valid_triplets = set()
    nums1_index = dict()
    for i in range(len(nums1)):
        if nums1[i] not in nums1_index:
            nums1_index[nums1[i]] = [i]
        else:
            nums1_index[nums1[i]].append(i)
    nums2_index = dict()
    for i in range(len(nums2)):
        if nums2[i] not in nums2_index:
            nums2_index[nums2[i]] = [i]
        else:
            nums2_index[nums2[i]].append(i)

    for i in range(len(nums1)):
        square = nums1[i] ** 2
        for j in range(len(nums2)):
            if square % nums2[j] != 0:
                continue
            else:
                if square / nums2[j] not in nums2_index:
                    continue
                else:
                    for index in nums2_index[square / nums2[j]]:
                        if index > j:
                            type1_valid_triplets.add((i, j, index))

    for i in range(len(nums2)):
        square = nums2[i] ** 2
        for j in range(len(nums1)):
            if square % nums1[j] != 0:
                continue
            else:
                if square / nums1[j] not in nums1_index:
                    continue
                else:
                    for index in nums1_index[square/nums1[j]]:
                        if index > j:
                            type2_valid_triplets.add((i, j, index))
    return len(type1_valid_triplets) + len(type2_valid_triplets)


def numTriplets2(nums1, nums2):

    def factorial(n):
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f

    nums1_index = dict()
    for i in range(len(nums1)):
        if nums1[i] not in nums1_index:
            nums1_index[nums1[i]] = [i]
        else:
            nums1_index[nums1[i]].append(i)

    nums2_index = dict()
    for i in range(len(nums2)):
        if nums2[i] not in nums2_index:
            nums2_index[nums2[i]] = [i]
        else:
            nums2_index[nums2[i]].append(i)

    pairs1 = set()
    for i in range(len(nums1)):
        square = nums1[i] ** 2
        for num in nums2_index:
            if square % num == 0 and square / num in nums2_index:
                pairs1.add(tuple(sorted([num, square//num])))

    pairs2 = set()
    for i in range(len(nums2)):
        square = nums2[i] ** 2
        for num in nums1_index:
            if square % num == 0 and square / num in nums1_index:
                pairs2.add(tuple(sorted([num, square//num])))

    def get_triplets_num(list1, list2):
        triplets = 0
        for index in list1:
            for i in range(len(list2)):
                if list2[i] > index:
                    triplets += len(list2) - i
                    break
        return triplets

    def get_one_type_of_triplets_num(pairs, dict1, dict2):
        total_valid_triplets = 0
        for pair in pairs:
            num1 = pair[0]
            num2 = pair[1]
            n = len(dict1[math.sqrt(num1 * num2)])
            triplets = 0
            if num1 == num2:
                if len(dict2[num1]) > 1:
                    triplets += factorial(len(dict2[num1])) / (factorial(2) * factorial(len(dict2[num1]) - 2))
            else:
                first_index_list = dict2[num1]
                second_index_list = dict2[num2]
                triplets += get_triplets_num(first_index_list, second_index_list)
                triplets += get_triplets_num(second_index_list, first_index_list)

            total_valid_triplets += n * triplets
        return total_valid_triplets

    type1_valid_triplets = get_one_type_of_triplets_num(pairs1, nums1_index, nums2_index)
    type2_valid_triplets = get_one_type_of_triplets_num(pairs2, nums2_index, nums1_index)
    return type1_valid_triplets + type2_valid_triplets

nums1 = [7,4]
nums2 = [5,2,8,9]
print(numTriplets2(nums1, nums2))

nums1 = [1,1]
nums2 = [1,1,1]
print(numTriplets2(nums1, nums2))

nums1 = [7,7,8,3]
nums2 = [1,2,9,7]
print(numTriplets2(nums1, nums2))

nums1 = [4,7,9,11,23]
nums2 = [3,5,1024,12,18]
print(numTriplets2(nums1, nums2))

nums1 = [4,1,4,1,12]
nums2 = [3,2,5,4]
print(numTriplets2(nums1, nums2))
