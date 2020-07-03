"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
    Input: [2, 6, 4, 8, 10, 9, 15]
    Output: 5
    Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Note:
    Then length of the input array is in range [1, 10,000].
    The input array may contain duplicates, so ascending order here means <=.
"""

"""

def findUnsortedSubarray(nums):
    l = len(nums)
    last_num = nums[0]
    temp_border = 0
    left_border = None
    for i in range(0, l):
        #print(nums[i])
        if nums[i] < last_num:
            left_border = temp_border
            break
        elif nums[i] > last_num:
            temp_border = i
            last_num = nums[i]

    if left_border == None:
        return 0


    last_num = nums[-1]
    right_border = None
    for i in reversed(range(0, l)):
        #print(i)
        if nums[i] > last_num:
            right_border = i + 1
            break
        else:
            last_num = nums[i]

    #print(right_border)

    max = nums[left_border]
    #print(max)
    for i in range(left_border, right_border):
        if nums[i] > max:
            max = nums[i]
    print("max:" + str(max))


    for i in reversed(range(0, l)):
        #print(i)
        #print(nums[i])
        if nums[i] < max:
            right_border = i

            break
    print("right border: " + str(right_border))

    min = nums[right_border]
    #print(max)
    for i in reversed(range(right_border, l)):
        if nums[i] < min:
            min = nums[i]

    print("min: " + str(min))
    for i in range(0, l):
        if nums[i] > min:
            left_border = i
            #print(i)
            break

    print("left border: " + str(left_border))


    return right_border - left_border + 1

"""

def findUnsortedSubarray(nums):
    if len(nums) < 2:
        return 0

    unmatch_index_list = list()
    max_value = nums[0]
    for i in range(1, len(nums)):
        if nums[i] >= max_value:
            max_value = nums[i]
        else:
            unmatch_index_list.append(i)
    if len(unmatch_index_list) == 0:
        return 0

    start = unmatch_index_list[0]
    end = unmatch_index_list[-1]
    min_value = min(nums[start:end + 1])

    for i in range(start):
        if nums[start - i - 1] > min_value:
            unmatch_index_list.insert(0, start - i - 1)
        else:
            break
    return unmatch_index_list[-1]+1 - unmatch_index_list[0]


input1 = [2, 6, 4, 8, 10, 9, 15]
input2 = [1,2,3,4]
input3 = [1, 3, 2, 4, 5]
input4 = [2, 3, 3, 2, 4]
input5 = [2, 1]
input6 = [1 ,2, 4, 5, 3]
input7 = [1, 3, 5, 4, 2]
input8 = [1, 2, 3, 5, 4]
print(findUnsortedSubarray(input1))
