"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]

]

"""

def generate(numRows):
    result = list()
    for i in range(1, numRows+1):
        temp = list()
        for j in range(0, i):
            if j == 0 or j == i-1:
                temp.append(1)
            else:
                temp.append(result[i-2][j-1]+result[i-2][j])
        result.append(temp)
    return result


print(generate(5))
