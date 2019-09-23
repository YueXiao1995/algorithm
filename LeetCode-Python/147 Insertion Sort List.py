"""
Sort a linked list using insertion sort.

Algorithm of Insertion Sort:
    Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
    At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
    It repeats until no input elements remain.

Example 1:
    Input: 4->2->1->3
    Output: 1->2->3->4

Example 2:
    Input: -1->5->3->4->0
    Output: -1->0->3->4->5
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        return

def printNodeList(node):
    string = ''
    while node:
        string += ' -> '+ str(node.val)
        node = node.next
    print(string)


def insertionSortList(head):
    sorted_head = None
    sorted_list_l = 0
    while head:
        if sorted_head == None:
            new_node = ListNode(head.val)
            sorted_head = new_node
            sorted_list_l += 1
        else:
            sorted_list = sorted_head
            i = 0
            while i < sorted_list_l:
                if head.val < sorted_list.val:
                    new_node = ListNode(sorted_list.val)
                    new_node.next = sorted_list.next
                    sorted_list.val = head.val
                    sorted_list.next = new_node
                    sorted_list_l += 1
                    break
                i += 1
                if i == sorted_list_l:
                    new_node = ListNode(head.val)
                    sorted_list.next = new_node
                    sorted_list_l += 1
                    break

                sorted_list = sorted_list.next
        head = head.next
    return sorted_head


head = ListNode(-1)
node2 = ListNode(5)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(0)


head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


printNodeList(insertionSortList(head))
