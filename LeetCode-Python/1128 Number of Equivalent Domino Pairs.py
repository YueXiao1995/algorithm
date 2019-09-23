"""
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

Example 1:
    Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
    Output: 1

Constraints:
    1 <= dominoes.length <= 40000
    1 <= dominoes[i][j] <= 9
"""

def numEquivDominoPairs(dominoes):
    l = len(dominoes)
    # sort all of the dominoes
    for i in range(0, l):
        dominoes[i] = sorted(dominoes[i])

    num_of_pairs = 0
    # iterate the dominoes while delete the equivalent dominoes until there are lest than 2 domino exist.
    while l > 1:
        equivalent_list = list()
        # find the equivalent dominoe and store their positions in to a list
        for i in range(1, l):
            if dominoes[i] == dominoes[0]:
                equivalent_list.append(i)
        # get the length of this list
        length_of_equivalent_list = len(equivalent_list)

        # if the length is zero, it means there is no equivalent dominoes has have been found for this dominoe
        if length_of_equivalent_list == 0:
            # delete this dominoe
            del dominoes[0]
            l -= 1
        else:
            # add the number of equivalent pairs
            num_of_pairs += sum(range(length_of_equivalent_list + 1))
            # delete these equivalent dominoes
            for i in reversed(range(0, length_of_equivalent_list)):
                del dominoes[equivalent_list[i]]
            del dominoes[0]
            l -= length_of_equivalent_list + 1

    return num_of_pairs


input1 = [[1,2],[2,1],[4,3],[3,4],[5,6]] # output = 1
input2 = [[1,2],[1,2],[1,1],[1,2],[2,2]] # output = 3
input3 = [[1,1],[2,2],[1,1],[1,2],[1,2],[1,1]]

print(numEquivDominoPairs(input3))
