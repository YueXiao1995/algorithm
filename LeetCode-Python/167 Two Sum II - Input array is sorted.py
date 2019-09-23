"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

"""
def twoSum(numbers, target):
    if target > 0:
        maxmum = len(numbers)-1
        for i in range(0, len(numbers)):
            if numbers[i] >= target:
                maxmum = i
                break
        for i in reversed(range(0, maxmum+1)):
            for j in reversed(range(0, i)):
                if numbers[i] + numbers[j] == target:
                    return [j+1, i+1]
    else:
        maxmum = 0
        for i in range(0, len(numbers)):
            if numbers[i] > target:
                maxmum = i
                break
        for i in reversed(range(0, maxmum + 1)):
            for j in reversed(range(0, i)):
                if numbers[i] + numbers[j] == target:
                    return [j + 1, i + 1]


input1 = [-1, 0]
input2 = [0, 0, 3, 4]
print(twoSum(input2, 0))
