"""
编写一个函数，检查输入的链表是否是回文的。

示例 1：
    输入： 1->2
    输出： false

示例 2：
    输入： 1->2->2->1
    输出： true

进阶：
    你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-linked-list-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def NodeListBuilder(nums):
    if len(nums) == 0:
        return None
    else:
        head = ListNode(nums[0])
        last = head
        for i in range(1, len(nums)):
            new_node = ListNode(nums[i])
            last.next = new_node
            last = new_node
        return head


def NodeListPrinter(head):
    node_list = []
    while head != None:
        node_list.append(str(head.val))
        head = head.next
    return ('->').join(node_list)


# 历遍得到链表总长度，利用栈来判断是否为回文，如果长度为奇数，则跳过中间点
def isPalindrome(head):
    l = 0
    p1 = head
    while p1 != None:
        l += 1
        p1 = p1.next
    stack = []
    i = 0
    p2 = head
    while p2 != None:
        if i != l//2  or l % 2 == 0:
            if len(stack) == 0:
                stack.append(p2.val)
            else:
                if p2.val == stack[-1]:
                    del stack[-1]
                else:
                    stack.append(p2.val)
        p2 = p2.next
        i += 1
    if len(stack) != 0:
        return False
    else:
        return True

nums = [1]
list = NodeListBuilder(nums)
print(isPalindrome(list))

nums = [1, 2, 2, 1]
list = NodeListBuilder(nums)
print(isPalindrome(list))
