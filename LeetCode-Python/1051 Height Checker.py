"""
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students not standing in the right positions.  (This is the number of students that must move
in order for all students to be standing in non-decreasing order of height.)

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
    # sort the list to generate a non-decreasing list
    non_decreasing = sorted(heights)
    # find and record the position where the two list are not match
    num_of_students_need_move = 0
    for i in range(0, len(heights)):
        if heights[i] != non_decreasing[i]:
            num_of_students_need_move += 1
    return num_of_students_need_move

input1 = [1,1,4,2,1,3]
print(heightChecker(input1))
