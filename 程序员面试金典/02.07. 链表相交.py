"""
给定两个（单向）链表，判定它们是否相交并返回交点。请注意相交的定义基于节点的引用，而不是基于节点的值。换句话说，如果一个链表的第k个节点与另一个链表的第j个节点是同一节点（引用完全相同），则这两个链表相交。

示例 1：
    输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
    输出：Reference of the node with value = 8
    输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

示例 2：
    输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
    输出：Reference of the node with value = 2
    输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

示例 3：
    输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
    输出：null
    输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
    解释：这两个链表不相交，因此返回 null。

注意：
    如果两个链表没有交点，返回 null 。
    在返回结果后，两个链表仍须保持原有的结构。
    可假定整个链表结构中没有循环。
    程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci
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


def getIntersectionNode(headA, headB):
    # 历遍两个链表得到它们的长度及尾部node的索引
    if headA == None or headB == None:
        return None
    l1 = 1
    p1 = headA
    while p1.next != None:
        l1 += 1
        p1 = p1.next

    l2 = 1
    p2 = headB
    while p2.next != None:
        l2 += 1
        p2 = p2.next

    pa = headA
    pb = headB

    # 判断索引是否相同
    if p1 == p2:
        if l1 > l2:
            for i in range(l1 - l2):
                pa = pa.next
        elif l2 > l1:
            for i in range(l2 - l1):
                pb = pb.next
        while pa != None and pb != None:
            if pa == pb:
                return pa
            else:
                pa = pa.next
                pb = pb.next
        return None
    else:
        return None


list_common = NodeListBuilder([8, 4, 5])

listA = ListNode(4)
node1 = ListNode(1)
listA.next = node1
node1.next = list_common

listB = ListNode(5)
node2 = ListNode(0)
node3 = ListNode(1)
listB.next = node2
node2.next = node3
node3.next = list_common

print(NodeListPrinter(getIntersectionNode(listA, listB)))

