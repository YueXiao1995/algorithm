"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.


Example 1:
    Input: 121
    Output: true

Example 1:
    Input: 121
    Output: true

Example 3:

Input: 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

def isPalindrome(x):
    isPalindrome = True
    if x >= 0:
        nums = list(map(int, str(x)))
        l = len(nums)
        if l == 1:
            return isPalindrome
        if l % 2 != 0:
            l = int(round(l / 2 - 0.5))
        else:
            l = int(l / 2)

        for i in range(0, l):
            if nums[i] != nums[-i - 1]:
                isPalindrome = False
                break
        return isPalindrome
    else:
        return False

print(isPalindrome(0))
