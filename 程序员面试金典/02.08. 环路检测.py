"""
给定一个有环链表，实现一个算法返回环路的开头节点。
有环链表的定义：在链表中某个节点的next元素指向在它前面出现过的节点，则表明该链表存在环路。


示例 1：
    输入：head = [3,2,0,-4], pos = 1
    输出：tail connects to node index 1
    解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
    输入：head = [1,2], pos = 0
    输出：tail connects to node index 0
    解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
    输入：head = [1], pos = -1
    输出：no cycle
    解释：链表中没有环。

进阶：
    你是否可以不用额外空间解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 将所有指针存入一个set
def detectCycle(head):
    pointers = set()
    while head != None:
        if head in pointers:
            return head
        pointers.add(head)
        head = head.next
    return None

# 不使用额外数据结构
def detectCycle2(head):
    # 快指针不会跳过慢指针
    # 当慢指针在环内时， 快指针总能在一周之内追上慢指针
    # m = head 到 环路的开头， r = 环路的长， d = 环路的开头到快指针追上慢指针的位置
    #   s1 = m + d
    #   s2 = m + n * r + d
    #   2 * s1 = s2
    #   m = n * r - d
    #   m = (n - 1 ) * r + (r - d)
    slow_pointer = head
    fast_pointer = head
    is_begin = True
    while fast_pointer != None and fast_pointer.next != None:
        if slow_pointer == fast_pointer:
            if is_begin:
                is_begin = False
            else:
                slow_pointer = head
                while True:
                    if slow_pointer == fast_pointer:
                        return slow_pointer
                    slow_pointer = slow_pointer.next
                    fast_pointer = fast_pointer.next
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next
    return None

head = ListNode(3)
node1 = ListNode(2)
node2 = ListNode(0)
node3 = ListNode(-4)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node1

print(detectCycle2(head).val)
