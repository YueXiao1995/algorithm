# 5854. Minimum Difference Between Highest and Lowest of K Scores


def minimumDifference(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    sorted_num = sorted(nums, reverse=True)
    diff = []
    for i in range(len(sorted_num) - k + 1):
        diff.append(sorted_num[i] - sorted_num[i+k-1])
    return min(diff)


nums = [90]
k = 1
#print(minimumDifference(nums, k))

nums = [9,4,1,7]
k = 2
#print(minimumDifference(nums, k))


# 5855. Find the Kth Largest Integer in the Array


def kthLargestNumber(nums, k):
    """
    :type nums: List[str]
    :type k: int
    :rtype: str
    """
    new_nums = list()
    for n in nums:
        new_nums.append(int(n))
    return str(sorted(new_nums, reverse=True)[k-1])



nums = ["3","6","7","10"]
k = 4
#print(kthLargestNumber(nums, k))

nums = ["2","21","12","1"]
k = 3
#print(kthLargestNumber(nums, k))

nums = ["0","0"]
k = 2
#print(kthLargestNumber(nums, k))


# 5856. Minimum Number of Work Sessions to Finish the Tasks

def minSessions(tasks, sessionTime):
    """
    :type tasks: List[int]
    :type sessionTime: int
    :rtype: int
    """
tasks = [1,2,3]
sessionTime = 3
print(minSessions(tasks, sessionTime))


tasks = [3,1,3,1,1]
sessionTime = 8
print(minSessions(tasks, sessionTime))



tasks = [1,2,3,4,5]
sessionTime = 15
print(minSessions(tasks, sessionTime))


def reversePrefix(word, ch):
    reversed_part = ''
    remain_part = word
    for i in range(len(word)):
        if word[i] == ch:
            remain_part = word[i+1:]
            for j in range(i+1):
                reversed_part += word[i - j]
            break

    return reversed_part + remain_part

word = "abcdefd"
ch = "d"
print(reversePrefix(word, ch))

word = "xyxzxe"
ch = "z"
print(reversePrefix(word, ch))

word = "abcd"
ch = "z"
print(reversePrefix(word, ch))





def interchangeableRectangles(rectangles):
    def factorial(n):
        """求阶乘"""
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f
    def c(n, m):
        return factorial(n) / (factorial(n-m) * factorial(m))

    ratio_count = dict()
    for rect in rectangles:
        r = rect[0]/rect[1]
        if r not in ratio_count:
            ratio_count[r] = 0
        ratio_count[r] += 1

    interchangeable_count = 0
    for r in ratio_count:
        if ratio_count[r] > 1:
            interchangeable_count += int(c(ratio_count[r], 2))

    return interchangeable_count

rectangles = [[4,8],[3,6],[10,20],[15,30]]
print(interchangeableRectangles(rectangles))


rectangles = [[4,5],[7,8]]
print(interchangeableRectangles(rectangles))

rectangles = [[16,1],[13,7],[20,18],[21,15],[20,3],[18,12],[23,14],[16,14],[5,25],[3,8],[6,17],[22,10],[25,17],[8,13],[8,11],[4,14],[2,17],[9,22],[3,15],[18,1],[19,13],[26,6],[26,14],[9,10],[12,6],[24,3],[21,8],[17,6],[16,7],[8,9],[20,24],[25,26],[22,23],[4,25],[23,23],[24,8],[14,4],[10,18],[13,6],[7,6],[24,15],[16,22],[17,19],[2,16],[23,21],[15,26],[7,17],[14,7],[10,26],[9,8],[7,10],[1,1],[11,17],[4,20],[19,24],[18,24],[9,21],[20,22],[21,12],[10,23],[5,9],[2,3],[6,17],[5,20],[11,15],[7,19],[5,9],[12,13],[15,19],[3,26],[19,25],[13,6],[22,13],[18,7],[4,9],[13,24],[22,21],[21,9],[25,26],[21,20],[9,13],[10,5],[11,18],[6,20],[16,8]]
print(interchangeableRectangles(rectangles))


def maxProduct(s):
    return 0

s = "leetcodecom"
print(maxProduct(s))


s = "bb"



s = "accbcaxxcxx"
