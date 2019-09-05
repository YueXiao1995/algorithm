"""
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students not standing in the right positions.  (This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)

Example 1:
    Input: [1,1,4,2,1,3]
    Output: 3
    Explanation:
        Students with heights 4, 3 and the last 1 are not standing in the right positions.
Note:
    1 <= heights.length <= 100
    1 <= heights[i] <= 100
"""

def heightChecker(heights):
    wrong_num = 0
    # record the height of last position
    last_height = 0
    # record the number of consecutive positions with equal height
    equal_length = 0
    # iterate the list
    for height in heights:
        # for the first position
        if last_height == 0:
            last_height = height
            equal_length = 1
        else:
            if height == last_height:
                equal_length += 1

            elif height < last_height:
                print("wrong"+str(height))
                wrong_num += equal_length
                equal_length = 1
                last_height = height
            else:
                print("right" + str(height))
                equal_length = 1
                last_height = height
        print(wrong_num)
    return wrong_num

input = [1,1,4,2,1,3]
input2 = [1,1,4,4,2,1]
print(heightChecker(input))
