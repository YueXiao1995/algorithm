"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor,
and you can either start from the step with index 0, or the step with index 1.

Example 1:
    Input: cost = [10, 15, 20]
    Output: 15
    Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:
    Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    Output: 6
    Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

Note:
    cost will have a length in the range [2, 1000].
    Every cost[i] will be an integer in the range [0, 999].
"""


def minCostClimbingStairs(cost):
    # add 0 to the list represent the top of the staircase
    cost.append(0)
    l = len(cost)

    # if start from the first position (index 0)
    min_cost_list = list()
    min_cost_list.append(0)
    min_cost_list.append(cost[0])

    for i in range(2, l):
        two_step = min_cost_list[i - 2] + cost[i - 2]
        one_step = min_cost_list[i - 1] + cost[i - 1]
        if two_step > one_step:
            min_cost_list.append(one_step)
        else:
            min_cost_list.append(two_step)


    # if start from the second position (index 1)
    min_cost_list2 = list()
    del cost[0]
    min_cost_list2.append(0)
    min_cost_list2.append(cost[0])
    for i in range(2, l-1):
        two_step = min_cost_list2[i - 2] + cost[i - 2]
        one_step = min_cost_list2[i - 1] + cost[i - 1]
        if two_step > one_step:
            min_cost_list2.append(one_step)
        else:
            min_cost_list2.append(two_step)

    # compare the minimum costs of starting from index 0 and index 1, return the minimum
    if min_cost_list[-1] > min_cost_list2[-1]:
        return min_cost_list2[-1]
    else:
        return min_cost_list[-1]

input1 = [10, 15, 20]
input2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
input3 = [100, 23]
print(minCostClimbingStairs(input2))
