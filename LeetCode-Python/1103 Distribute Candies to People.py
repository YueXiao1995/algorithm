"""
We distribute some number of candies, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.

Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

Return an array (of length num_people and sum candies) that represents the final distribution of candies.


Example 1:
    Input: candies = 7, num_people = 4
    Output: [1,2,3,1]
    Explanation:
    On the first turn, ans[0] += 1, and the array is [1,0,0,0].
    On the second turn, ans[1] += 2, and the array is [1,2,0,0].
    On the third turn, ans[2] += 3, and the array is [1,2,3,0].
    On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].

Example 2:
    Input: candies = 10, num_people = 3
    Output: [5,2,3]
    Explanation:
    On the first turn, ans[0] += 1, and the array is [1,0,0].
    On the second turn, ans[1] += 2, and the array is [1,2,0].
    On the third turn, ans[2] += 3, and the array is [1,2,3].
    On the fourth turn, ans[0] += 4, and the final array is [5,2,3].

Constraints:
    1 <= candies <= 10^9
    1 <= num_people <= 1000
"""

import math
def distributeCandies(candies, num_people):
    # the time of distribution happens
    time_of_distributions = math.ceil(math.sqrt(candies * 2 + 1 / 4) - 1 / 2)
    # the time of the process from the start to the end
    x = math.ceil(time_of_distributions/num_people)
    # the variable to record the total candies for each people
    final_distribution = list()
    # the last distribution in (x-1)th process
    previous_last_distribution = (x - 1) * num_people
    # the amount of candies after x-1 process
    remain = candies - (1 + previous_last_distribution) * (previous_last_distribution) / 2
    # iterate over the people
    for i in range(num_people):
        num_of_candies = 0
        # if the number of process more than 1, calculate the candies a people can get in previous processes
        if x - 1 > 0:
            num_of_candies += (((0 + (x - 2) * num_people) * (x - 1)) / 2) + (x - 1) * (i + 1)
        # calculate the num of candies people should get
        num = previous_last_distribution + i + 1
        # check if the remain candies is enough
        if remain > num:
            num_of_candies += num
            remain -= num
        else:
            num_of_candies += remain
            remain = 0
        final_distribution.append(int(num_of_candies))
    return final_distribution

candies1 = 7
num_people1 = 4

candies2 = 10
num_people2 = 3

print(distributeCandies(candies2, num_people2))
