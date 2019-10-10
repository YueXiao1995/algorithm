"""
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0],
and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

Example 1:
    Input: [[10,20],[30,200],[400,50],[30,20]]
    Output: 110
    Explanation:
    The first person goes to city A for a cost of 10.
    The second person goes to city A for a cost of 30.
    The third person goes to city B for a cost of 50.
    The fourth person goes to city B for a cost of 20.
    The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

Note:
    1 <= costs.length <= 100
    It is guaranteed that costs.length is even.
    1 <= costs[i][0], costs[i][1] <= 1000
"""

def twoCitySchedCost(costs):
    costs = sorted(costs, key=lambda l: l[0]-l[1])
    N = len(costs) // 2
    min_total_cost = 0
    for cost in costs[:N]:
        min_total_cost += cost[0]
    for cost in costs[N:]:
        min_total_cost += cost[1]
    return min_total_cost

def twoCitySchedCost2(costs):
    costs = sorted(costs, key=lambda l: l[0]-l[1])
    N = len(costs) // 2
    d_A = [sum(x) for x in zip(*costs[:N])][0]
    d_B = [sum(x) for x in zip(*costs[N:])][1]
    return d_A + d_B

input1 = [[10,20],[30,200],[400,50],[30,20]]
print(twoCitySchedCost2(input1))

