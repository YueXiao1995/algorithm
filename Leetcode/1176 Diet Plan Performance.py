"""
A dieter consumes calories[i] calories on the i-th day.  For every consecutive sequence of k days, they look at T, the total calories consumed during that sequence of k days:

If T < lower, they performed poorly on their diet and lose 1 point;
If T > upper, they performed well on their diet and gain 1 point;
Otherwise, they performed normally and there is no change in points.
Return the total number of points the dieter has after all calories.length days.

Note that: The total points could be negative.

Example 1:
    Input: calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3
    Output: 0
    Explaination: calories[0], calories[1] < lower and calories[3], calories[4] > upper, total points = 0.

Example 2:
    Input: calories = [3,2], k = 2, lower = 0, upper = 1
    Output: 1
    Explaination: calories[0] + calories[1] > upper, total points = 1.

Example 3:
    Input: calories = [6,5,0,0], k = 2, lower = 1, upper = 5
    Output: 0
    Explaination: calories[0] + calories[1] > upper, calories[2] + calories[3] < lower, total points = 0.

Constraints:
1 <= k <= calories.length <= 10^5
0 <= calories[i] <= 20000
0 <= lower <= upper
"""

# Time Limit Exceeded
"""
def dietPlanPerformance(calories, k, lower, upper):
    # the total number of days
    l = len(calories)
    total_points = 0
    # iterate the calories list
    for i in range(0, l - k + 1):
        # calculate the total calories consumption from day i to day i+k
        total_consumption = 0
        for j in range(i, i + k):
            total_consumption += calories[j]
        # if total consumption smaller than lower, total point decrease by 1
        if total_consumption < lower:
            total_points -= 1
        # if total consumption bigger than upper, total point increase by 1
        elif total_consumption > upper:
            total_points += 1
    return total_points
"""

def dietPlanPerformance(calories, k, lower, upper):
    # the total number of days
    l = len(calories)
    total_points = 0
    # iterate the calories list
    total_consumption = None
    for i in range(0, l - k + 1):
        # if the first sequence
        if total_consumption == None:
            # calculate the total calories consumption from day i to day i+k
            sum = 0
            for j in range(i, i + k):
                sum += calories[j]
            total_consumption = sum
        else:
            # add calories[i+k] to total consumption, and minus calories[i-1]
            total_consumption += calories[i + k - 1]
            total_consumption -= calories[i - 1]

        # if total consumption smaller than lower, total point decrease by 1
        if total_consumption < lower:
            total_points -= 1
        # if total consumption bigger than upper, total point increase by 1
        elif total_consumption > upper:
            total_points += 1
    return total_points

calories1 = [1,2,3,4,5]
k1 = 1
lower1 = 3
upper1 = 3

calories2 = [3,2]
k2 = 2
lower2 = 0
upper2 = 1

calories3 = [6,5,0,0]
k3 = 2
lower3 = 1
upper3 = 5


print(dietPlanPerformance(calories2,k2,lower2,upper2))
