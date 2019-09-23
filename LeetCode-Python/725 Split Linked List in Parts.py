"""
Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]

Example 1:
    Input:  root = [1, 2, 3], k = 5
    Output: [[1],[2],[3],[],[]]
    Explanation: The input and each element of the output are ListNodes, not arrays. For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null. The first element output[0] has output[0].val = 1, output[0].next = null. The last element output[4] is null, but it's string representation as a ListNode is [].

Example 2:
    Input: root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
    Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
    Explanation:
    The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
    Note:

The length of root will be in the range [0, 1000].
Each value of a node in the input will be an integer in the range [0, 999].
k will be an integer in the range [1, 50].
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        return

def printNodeList(node):
    string = ' -> '
    while node:
        string += str(node.val) + ' -> '
        node = node.next
    print(string)


def splitListToParts(root, k):
    list_listnode = list()
    result = list()
    while root:
        list_listnode.append(root)
        root = root.next
    l = len(list_listnode)

    if l == 0:
        for i in range(0, k):
            result.append(None)
        return result

    basic_l = l // k
    print("basic_l: "+str(basic_l))
    remain = l % k
    print("remain: "+str(remain))

    newhead = list_listnode[0]
    last_index = 0
    for i in range(0, k):
        if i < remain:
            last_index += basic_l + 1
            list_listnode[last_index - 1].next = None
            result.append(newhead)
            if last_index > l - 1:
                newhead = None
            else:
                newhead = list_listnode[last_index]
        else:
            if last_index > l - 1:
                result.append(None)
            else:
                last_index += basic_l
                list_listnode[last_index - 1].next = None
                result.append(newhead)
                if last_index > l - 1:
                    newhead = None
                else:
                    newhead = list_listnode[last_index]

    return result


head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5



list_nodelist = splitListToParts(head, 2)
for list in list_nodelist:
    printNodeList(list)


