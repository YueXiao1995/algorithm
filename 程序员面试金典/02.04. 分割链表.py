"""
编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。如果链表中包含 x，x 只需出现在小于 x 的元素之后(如下所示)。分割元素 x 只需处于“右半部分”即可，其不需要被置于左右两部分之间。

示例:
    输入: head = 3->5->8->5->10->2->1, x = 5
    输出: 3->1->2->10->5->5->8
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

# 操作修改链表
def partition(head, x):
    if head == None:
        return None
    pointer1 = head
    pointer2 = None
    new_head = None
    if pointer1.val >= x:
        pointer2 = head
    else:
        new_head = head

    while pointer1.next != None:
        if pointer1.next.val >= x:
            if pointer2 == None:
                pointer2 = pointer1.next
            pointer1 = pointer1.next
        else:
            if pointer2 != None:
                temp_node = ListNode(pointer2.val)
                temp_node.next = pointer2.next
                pointer2.val = pointer1.next.val
                pointer2.next = temp_node

                if pointer1 == pointer2:
                    pointer1 = temp_node

                if new_head == None:
                    new_head = pointer2

                pointer2 = pointer2.next
                pointer1.next = pointer1.next.next
            else:
                pointer1 = pointer1.next

    if new_head != None:
        return new_head
    else:
        return head
# 新建新链表
def partition2(head, x):
    smaller_head = None
    smaller_tail = None
    bigger_head = None
    bigger_tail = None
    pointer = head
    while pointer != None:
        new_node = ListNode(pointer.val)
        if pointer.val < x:
            if smaller_head == None:
                smaller_head = new_node
                smaller_tail = new_node
            else:
                smaller_tail.next = new_node
                smaller_tail = new_node
        else:
            if bigger_head == None:
                bigger_head = new_node
                bigger_tail = new_node
            else:
                bigger_tail.next = new_node
                bigger_tail = new_node
        pointer = pointer.next

    if smaller_head != None and bigger_head != None:
        smaller_tail.next = bigger_head
        return smaller_head
    elif smaller_head != None:
        return smaller_head
    elif bigger_head != None:
        return bigger_head
    else:
        return None

nums = [11, 3, 5, 8, 5, 10, 2, 1]
x = 5
head = NodeListBuilder(nums)
print(NodeListPrinter(head))
print(NodeListPrinter(partition(head, x)))

nums = [3, 5, 8, 5, 10, 2, 1, 7]
x = 5
head = NodeListBuilder(nums)
print(NodeListPrinter(head))
print(NodeListPrinter(partition2(head, x)))
