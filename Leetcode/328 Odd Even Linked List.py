"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:
    Input: 1->2->3->4->5->NULL
    Output: 1->3->5->2->4->NULL

Example 2:
    Input: 2->1->3->5->6->4->7->NULL
    Output: 2->3->6->7->1->5->4->NULL
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

def oddEvenList(head):
    index = 1
    even_list = None
    odd_head = None
    odd_list = None
    even_head = None
    while head:
        new_node = ListNode(head.val)
        if index%2 == 0:

            if even_list != None:
                even_list.next = new_node
                even_list = new_node
            else:
                even_head = new_node
                even_list = even_head
        else:
            if odd_list != None:
                odd_list.next = new_node
                odd_list = new_node
            else:
                odd_head = new_node
                odd_list = odd_head
        head = head.next
        index += 1

    if odd_head!= None:
        odd_list.next = even_head
        return odd_head
    else:
        return even_head



head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)


head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

#printNodeList(head)

newList = oddEvenList(head)
print("result: ")
printNodeList(newList)
