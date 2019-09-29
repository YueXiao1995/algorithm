"""
Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.

Example 1:
    Input: s = "abcd", k = 2
    Output: "abcd"
    Explanation: There's nothing to delete.

Example 2:
    Input: s = "deeedbbcccbdaa", k = 3
    Output: "aa"
    Explanation:
    First delete "eee" and "ccc", get "ddbbbdaa"
    Then delete "bbb", get "dddaa"
    Finally delete "ddd", get "aa"

Example 3:
    Input: s = "pbbcggttciiippooaais", k = 2
    Output: "ps"
"""
def removeDuplicates(s: str, k: int) -> str:
    while True:
        s = list(s)
        is_deleted = False
        l = len(s)
        i = 0
        last = None
        repeat_time = 0
        while i < l:
            if last == None:
                last = s[i]
                repeat_time = 1
            else:
                if s[i] == last:
                    repeat_time += 1
                    if repeat_time == k:
                        is_deleted = True
                        break
                else:
                    last = s[i]
                    repeat_time = 1
            i += 1
        if is_deleted == False:
            break
        else:
            for j in range(k):
                del s[i - k + 1]
    return ("").join(s)

s1 = "abcd"
k1 = 2

s2 = "deeedbbcccbdaa"
k2 = 3

s3 = "pbbcggttciiippooaais"
k3 = 2

print(removeDuplicates(s3, k3))
