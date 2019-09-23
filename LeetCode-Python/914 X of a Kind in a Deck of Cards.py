"""
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.

Example 1:
    Input: [1,2,3,4,4,3,2,1]
    Output: true
    Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]

Example 2:
    Input: [1,1,1,2,2,2,3,3]
    Output: false
    Explanation: No possible partition.

Example 3:
    Input: [1]
    Output: false
    Explanation: No possible partition.

Example 4:
    Input: [1,1]
    Output: true
    Explanation: Possible partition [1,1]

Example 5:
    Input: [1,1,2,2,2,2]
    Output: true
    Explanation: Possible partition [1,1],[2,2],[2,2]

Note:
    1 <= deck.length <= 10000
    0 <= deck[i] < 10000
"""

def hasGroupsSizeX(deck):
    # sort the deck
    deck = sorted(deck)
    # find the size of groups
    group_size = list()
    last_num = None
    temp_size = 0
    for num in deck:
        if last_num == None:
            last_num = num
            temp_size += 1
        else:
            if num == last_num:
                temp_size += 1
            else:
                # if the last group size smaller than 2, return False
                if temp_size < 2:
                    return False
                group_size.append(temp_size)
                temp_size = 1
            last_num = num
    # append the last temp_size to the size list, if it is smaller than 2, return False
    if temp_size > 1:
        group_size.append(temp_size)
    else:
        return False

    # find the common factor of the group sizes
    common_factor = None
    for size in group_size:
        # find and record the factors of a size, except 1
        factors = set()
        for i in range(2, size + 1):
            if size % i == 0:
                factors.add(i)
        # update the common factor list
        if common_factor == None:
            common_factor = factors
        else:
            common_factor = common_factor & factors
    # if common factor set is empty, return False, else return True
    if len(common_factor) != 0:
        return True
    else:
        return False

input1 = [1,2,3,4,4,3,2,1]
input2 = [1,1,1,2,2,2,3,3]
input3 = [1]
input4 = [1,1]
input5 = [1,1,2,2,2,2]
input6 = [1,1,1,1,2,2,2,2,2,2]
input7 = [0,0,0,0,1,1,1,1]

print(hasGroupsSizeX(input3))
