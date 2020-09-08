"""
Given a string s and an array of integers cost where cost[i] is the cost of deleting the character i in s.

Return the minimum cost of deletions such that there are no two identical letters next to each other.

Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.

Example 1:
    Input: s = "abaac", cost = [1,2,3,4,5]
    Output: 3
    Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).

Example 2:
    Input: s = "abc", cost = [1,2,3]
    Output: 0
    Explanation: You don't need to delete any character because there are no identical letters next to each other.

Example 3:
    Input: s = "aabaa", cost = [1,2,3,4,1]
    Output: 2
    Explanation: Delete the first and the last character, getting the string ("aba").

Constraints:
    s.length == cost.length
    1 <= s.length, cost.length <= 10^5
    1 <= cost[i] <= 10^4
    s contains only lowercase English letters.
"""


def minCost(s, cost):
    s = str(s)
    s_without_repeating_letters = [[s[0]]]
    cost_list = [[cost[0]]]
    for i in range(1, len(s)):
        if s[i] == s_without_repeating_letters[-1][0]:
            cost_list[-1].append(cost[i])
        else:
            s_without_repeating_letters.append(s[i])
            cost_list.append([cost[i]])
    min_total_cost = 0
    for costs in cost_list:
        if len(costs) > 1:
            min_total_cost += sum(costs) - max(costs)
    return min_total_cost


def minCost2(s, cost):
    s = str(s)
    min_total_cost = 0
    cost_list = [cost[0]]
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cost_list.append(cost[i])
        else:
            if len(cost_list) != 1:
                min_total_cost += sum(cost_list) - max(cost_list)

            cost_list = [cost[i]]

    if len(cost_list) != 1:
        min_total_cost += sum(cost_list) - max(cost_list)
    return min_total_cost

def minCost3(s, cost):
    s = str(s)
    min_total_cost = 0
    cost_sum = cost[0]
    max_cost = cost[0]
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cost_sum += cost[i]
            if cost[i] > max_cost:
                max_cost = cost[i]
        else:
            min_total_cost += cost_sum - max_cost
            cost_sum = cost[i]
            max_cost = cost[i]
    min_total_cost += cost_sum - max_cost
    return min_total_cost

s = "abaac"
cost = [1,2,3,4,5]
print(minCost3(s, cost))

s = "abc"
cost = [1,2,3]
print(minCost3(s, cost))

s = "aabaa"
cost = [1,2,3,4,1]
print(minCost3(s, cost))
