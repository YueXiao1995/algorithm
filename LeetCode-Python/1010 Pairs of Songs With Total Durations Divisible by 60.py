"""
In a list of songs, the i-th song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.
Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.

Example 1:
    Input: [30,20,150,100,40]
    Output: 3
    Explanation: Three pairs have a total duration divisible by 60:
    (time[0] = 30, time[2] = 150): total duration 180
    (time[1] = 20, time[3] = 100): total duration 120
    (time[1] = 20, time[4] = 40): total duration 60

Example 2:
    Input: [60,60,60]
    Output: 3
    Explanation: All three pairs have a total duration of 120, which is divisible by 60.

Note:
    1 <= time.length <= 60000
    1 <= time[i] <= 500
"""

# Time Limit Exceeded
"""
def numPairsDivisibleBy60(time):
    # for each duration, find the durations which can form a pair with it
    num_of_pairs = 0
    l = len(time)
    while l > 0:
        for i in range(1, l):
            sum = time[0] + time[i]
            if sum % 60 == 0:
                num_of_pairs += 1
        del time[0]
        print(time)
        l -= 1
    return num_of_pairs
"""

def numPairsDivisibleBy60(time):
    # find the unique nums and their freq in the time list
    unique = dict()
    for t in time:
        if t not in unique:
            unique[t] = 1
        else:
            unique[t] += 1

    # for each unique time duration, find the durations which can form a pair with it
    num_of_pair = 0
    # iterate the list(unique), so that we can delete a key
    for t_1 in list(unique):
        # iterate the dict
        for t_2 in unique:
            # check if the sum is divisible by 60
            if (t_1 + t_2) % 60 == 0:
                # if the second time duration is not itself
                if t_1 != t_2:
                    num_of_pair += unique[t_1] * unique[t_2]
                # if the the second time duration is it itself
                else:
                    num_of_pair += sum(range(unique[t_2]))
        # delete this key from list
        del unique[t_1]
    return num_of_pair

input1 = [30,20,150,100,40]
input2 = [60,60,60]

print(numPairsDivisibleBy60(input1))

#print(sum(range(4)))
