"""
编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

示例1:
     输入：[1, 2, 3, 3, 2, 1]
     输出：[1, 2, 3]

示例2:
     输入：[1, 1, 1, 1, 2]
     输出：[1, 2]

提示：
    链表长度在[0, 20000]范围内。
    链表元素在[0, 20000]范围内。

进阶：
    如果不得使用临时缓冲区，该怎么解决？
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
        for i in range(1,len(nums)):
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

# 使用一个额外的数据结构 set
def removeDuplicateNodes(head):
    if head == None:
        return None
    unique_num = set()
    unique_num.add(head.val)
    last_node = head
    while last_node.next != None:
        if last_node.next.val not in unique_num:
            unique_num.add(last_node.next.val)
            last_node = last_node.next
        else:
            last_node.next = last_node.next.next
    return head

# 使用两个指针， 四件复杂度 O(n^2) 超出时间限制
def removeDuplicateNodes2(head):
    pointer_1 = head
    while pointer_1 != None:
        pointer_2 = pointer_1
        while pointer_2.next != None:
            if pointer_2.next.val == pointer_1.val:
                pointer_2.next = pointer_2.next.next
            else:
                pointer_2 = pointer_2.next
        pointer_1 = pointer_1.next
    return head


nums = [1, 2, 3, 3, 2, 1]
head = NodeListBuilder(nums)
print(NodeListPrinter(head))
print(NodeListPrinter(removeDuplicateNodes2(head)))


nums = [1, 1, 1, 1, 2]
head = NodeListBuilder(nums)
print(NodeListPrinter(head))
print(NodeListPrinter(removeDuplicateNodes2(head)))


nums = []
head = NodeListBuilder(nums)
print(NodeListPrinter(head))
print(NodeListPrinter(removeDuplicateNodes2(head)))
