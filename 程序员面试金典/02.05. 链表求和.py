"""
给定两个用链表表示的整数，每个节点包含一个数位。

这些数位是反向存放的，也就是个位排在链表首部。

编写函数对这两个整数求和，并用链表形式返回结果。

示例：
    输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
    输出：2 -> 1 -> 9，即912

进阶：假设这些数位是正向存放的，请再做一遍。

示例：
    输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
    输出：9 -> 1 -> 2，即912

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-lists-lcci
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
    node_list = list()
    while head != None:
        node_list.append(str(head.val))
        head = head.next
    return ('->').join(node_list)

# 不转化为数字
def addTwoNumbers(l1, l2):
    p1 = l1
    p2 = l2
    new_list = None
    p3 = None
    extra = 0
    while p1 != None or p2 != None:
        num1 = 0
        num2 = 0
        if p1 != None:
            num1 += p1.val
            p1 = p1.next

        if p2 != None:
            num2 += p2.val
            p2 = p2.next

        sum = num1 + num2 + extra
        new_node = ListNode(sum % 10)
        extra = sum // 10
        if new_list == None:
            new_list = new_node
            p3 = new_node
        else:
            p3.next = new_node
            p3 = p3.next

    if extra != 0:
        node = ListNode(extra)
        p3.next = node

    return new_list

# 转化为数字
def addTwoNumbers2(l1, l2):
    num1 = ''
    num2 = ''
    while l1 != None:
        num1 = str(l1.val) + num1
        l1 = l1.next
    while l2 != None:
        num2 = str(l2.val) + num2
        l2 = l2.next
    sum = str(int(num1) + int(num2))
    head = None
    p1 = None
    for i in range(len(sum)):
        node = ListNode(int(sum[-i-1]))
        if head == None:
            head = node
            p1 = node
        else:
            p1.next = node
            p1 = p1.next
    return head

num1 = [7, 1, 6]
num2 = [5, 9, 2]
l1 = NodeListBuilder(num1)
l2 = NodeListBuilder(num2)
print(NodeListPrinter(addTwoNumbers2(l1, l2)))

num1 = [5]
num2 = [5]
l1 = NodeListBuilder(num1)
l2 = NodeListBuilder(num2)
print(NodeListPrinter(addTwoNumbers(l1, l2)))
