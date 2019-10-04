"""
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:

Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.

Example 1:
    Input: [1,2,3],[2]
    Output: 1
    Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.

Example 2:
    Input: [1,2,3,4],[1,4]
    Output: 1
    Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
"""

# Time Limit Exceeded
def findRadius(houses, heaters):
    houses = sorted(houses)
    heaters = sorted(heaters)
    max_min_distance = 0
    for house in houses:
        print(max_min_distance)
        min_distance = None
        heater_index = 0
        while heater_index < len(heaters):
            distance = abs(heaters[heater_index] - house)
            if min_distance == None:
                min_distance = distance
            else:
                if distance < min_distance:
                    min_distance = distance
                else:
                    break
            heater_index += 1
        if min_distance > max_min_distance:
            max_min_distance = min_distance
    return max_min_distance

def findRadius2(houses, heaters):
    # sort the houses and heaters list
    houses = sorted(houses)
    heaters = sorted(heaters)
    # the closest heater of the last house in list
    last_heater_index = 0
    # the maximum value of minimum distance between a house and any heater
    max_min_distance = 0
    # iterate over the houses list
    for house in houses:
        # the minimum distance between the house and a heater
        min_distance = None
        # the index of the beginning point of the distance calculation
        heater_index = last_heater_index
        # iterate over the heaters, find the closest heater
        while heater_index < len(heaters):
            # calculate the distance
            distance = abs(heaters[heater_index] - house)
            if min_distance == None:
                min_distance = distance
            else:
                if distance <= min_distance:
                    min_distance = distance
                else:
                    break
            heater_index += 1
        # get the position of the closest heater
        last_heater_index = heater_index - 1
        # update the max min distance
        if min_distance > max_min_distance:
            max_min_distance = min_distance
    return max_min_distance

houses1 = [1, 2, 3]
heaters1 = [2]

houses2 = [1, 2, 3, 4]
heaters2 = [1, 4]

houses3 = [1,1,1,1,1,1,999,999,999,999,999]
heaters3 = [499,500,501]

houses4 = [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
heaters4 = [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]

print(findRadius2(houses4, heaters4))
