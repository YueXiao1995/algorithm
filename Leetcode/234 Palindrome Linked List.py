"""
Given a singly linked list, determine if it is a palindrome.

Example 1:
    Input: 1->2
    Output: false

Example 2:
    Input: 1->2->2->1
    Output: true
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        return

def printNodeList(node):
    while node:
        print(node.val)
        node = node.next

head= ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)

head.next = node2
node2.next = node3
node3.next = node4

def isPalindrome(head):
    nums = list()
    len = 0
    isPalindrome = True
    while head:
        nums.append(head.val)
        head = head.next
        len += 1
    if len == 1:
        return isPalindrome
    if len%2 != 0:
        len = int(round(len/2-0.5))
    else:
        len = int(len/2)

    for i in range(0, len):
        if nums[i] != nums[-i-1]:
            isPalindrome = False
            break
    return isPalindrome

print(isPalindrome(head))

