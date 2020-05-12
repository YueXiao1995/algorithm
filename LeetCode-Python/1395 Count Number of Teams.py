"""
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

Example 1:
    Input: rating = [2,5,3,4,1]
    Output: 3
    Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).

Example 2:
    Input: rating = [2,1,3]
    Output: 0
    Explanation: We can't form any team given the conditions.

Example 3:
    Input: rating = [1,2,3,4]
    Output: 4

Constraints:
    n == rating.length
    1 <= n <= 200
    1 <= rating[i] <= 10^5
"""

def numTeams(rating):
    def insertIntoLine(line, rating):
        l = len(line)
        if l == 0:
            line.append(rating)
            return [], []
        else:
            if rating < line[0]:
                line.insert(0, rating)
                return [], line[1:]
            elif rating > line[-1]:
                line.append(rating)
                return line[:-1], []
            else:
                for i in range(len(line) - 1):
                    if line[i] < rating and line[i + 1] > rating:
                        line.insert(i+1, rating)
                        return line[:i + 1] , line[i + 2:]

    smaller_ratings = dict()
    bigger_ratings = dict()
    line = list()
    num_of_teams = 0
    for i in range(len(rating)):
        bigger_sum = 0
        smaller_sum = 0
        smaller_ratings_line, bigger_ratings_line = insertIntoLine(line, rating[-i - 1])

        for j in range(len(bigger_ratings_line)):
            num_of_teams += bigger_ratings[bigger_ratings_line[j]]


        for j in range(len(smaller_ratings_line)):
            num_of_teams += smaller_ratings[smaller_ratings_line[j]]

        bigger_sum += len(bigger_ratings_line)
        smaller_sum += len(smaller_ratings_line)

        bigger_ratings[rating[-i - 1]] = bigger_sum
        smaller_ratings[rating[-i - 1]] = smaller_sum

    return num_of_teams

rating = [2,5,3,4,1]
print(numTeams(rating))

rating = [2,1,3]
print(numTeams(rating))

rating = [1,2,3,4]
print(numTeams(rating))
