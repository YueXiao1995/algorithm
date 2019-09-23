"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:
    Input: nums = [1,2,3,1], k = 3, t = 0
    Output: true

Example 2:
    Input: nums = [1,0,1,1], k = 1, t = 2
    Output: true

Example 3:
    Input: nums = [1,5,9,1,5,9], k = 2, t = 3
    Output: false
"""


# too slow
"""
def containsNearbyAlmostDuplicate(nums, k, t):
    unique_nums = dict()
    for i in range(0, len(nums)):
        if nums[i] not in unique_nums:
            unique_nums[nums[i]] = [i]
        else:
            unique_nums[nums[i]].append(i)
    print(unique_nums)

    for unique_num in unique_nums:
        print(unique_num)

        for new_unique_num in unique_nums:
            if abs(new_unique_num - unique_num) <= t:

                if new_unique_num == unique_num:
                    print("num2:" + str(new_unique_num))
                    for i in range(0, len(unique_nums[unique_num])):
                        for j in range(i + 1, len(unique_nums[unique_num])):
                            if unique_nums[unique_num][j] - unique_nums[unique_num][i] <= k:
                                return True
                else:
                    print("num2:" + str(new_unique_num))
                    for i in range(0, len(unique_nums[unique_num])):
                        print("i: "+str(i))
                        for j in range(0, len(unique_nums[new_unique_num])):
                            print("j: " + str(j))
                            if abs(unique_nums[unique_num][i] - unique_nums[new_unique_num][j]) <= k:
                                return True
    return False
"""
def containsNearbyAlmostDuplicate(nums, k, t):
    # store the nums and their position into a dict
    unique_nums = dict()
    for i in range(0, len(nums)):
        if nums[i] not in unique_nums:
            unique_nums[nums[i]] = [i]
        else:
            unique_nums[nums[i]].append(i)

    print(unique_nums)
    # sort the keys of the dict
    sorted_keys = sorted(unique_nums)
    # the number of distinct keys
    num_of_unique = len(sorted_keys)
    print(sorted_keys)

    # iterate through the sorted keys to find out the result
    for i in range(0, num_of_unique):
        i_list = unique_nums[sorted_keys[i]]
        print(i_list)
        for j in range(i, num_of_unique):
            # check if the difference of two keys is at most t
            if sorted_keys[j] - sorted_keys[i] <= t:
                print(sorted_keys[j] - sorted_keys[i])
                # check if there are two indexs which have a difference at most k
                if i == j:
                    for index in range(0, len(i_list)-1):
                        if i_list[index + 1] - i_list[index] <= k:
                            return True
                else:
                    for index_i in i_list:
                        for index_j in unique_nums[sorted_keys[j]]:
                            if abs(index_i - index_j) <= k:
                                return True
            else:
                # break the loop
                break
    return False


input1 = [1,2,3,1]
k1 = 3
t1 = 0

input2 = [1,0,1,1]
k2 = 1
t2 = 2

input3 = [1,5,9,1,5,9]
k3 = 2
t3 = 3

input4 = [10,100,11,9,100,10]
k4 = 1
t4 = 2

print(containsNearbyAlmostDuplicate(input3, k3, t3))

