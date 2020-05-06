"""
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".
Example 1:
    Input: [5, 4, 3, 2, 1]
    Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
    Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
    For the left two athletes, you just need to output their relative ranks according to their scores.

Note:
    N is a positive integer and won't exceed 10,000.
    All the scores of athletes are guaranteed to be unique.
"""

def findRelativeRanks(nums):
    ranks = sorted(nums)[::-1]
    score_ranks = dict()
    for i in range(len(ranks)):
        if i == 0:
            score_ranks[ranks[i]] = "Gold Medal"
        elif i == 1:
            score_ranks[ranks[i]] = "Silver Medal"
        elif i == 2:
            score_ranks[ranks[i]] = "Bronze Medal"
        else:
            score_ranks[ranks[i]] = str(i + 1)

    print(score_ranks)

    for i in range(len(nums)):
        nums[i] = score_ranks[nums[i]]
    return nums


nums1 = [5, 4, 3, 2, 1]
print(findRelativeRanks(nums1))
