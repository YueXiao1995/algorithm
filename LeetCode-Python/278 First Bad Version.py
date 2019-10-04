"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
"""

def isBadVersion(version):
    if versions[version] == "good":
        return False
    else:
        return True

def firstBadVersion(n):
    # define the start and end point of search
    start = 1
    end = n
    # begin to search
    while start < end:
        # find the middle point
        middle = (start + end) // 2
        # check if the middle point is false
        if isBadVersion(middle) == False:
            # update the start point of search
            start = middle + 1
        else:
            # update the end point of search
            end = middle
    # return the start point
    return start

versions = {1: "good", 2: "good", 3: "bad", 4: "bad", 5: "bad"}

print(firstBadVersion(5))
