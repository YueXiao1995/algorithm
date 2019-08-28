"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:
    Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 8 -> 0 -> 7

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




def addTwoNumbers(l1, l2):
    # read the vals and store them into lists by order
    num1 = list()
    while(l1):
        num1.append(l1.val)
        l1 = l1.next

    num2 = list()
    while(l2):
        num2.append(l2.val)
        l2 = l2.next

    # A loop
    #   calculate the sum of the values in the same position in two lists and the carry bit value
    #   reset the carry bit to zero
    #   if the sum > 9
    #      sum = sum -10
    #      carry bit = 1
    #   generate a new node as the new head
    # after the loop if carry bit is not 0
    #   generate a new node as the the head

    temp = 0
    index = 0
    l1 = len(num1)
    l2 = len(num2)
    head = None
    while(index < l1 or index < l2):
        num_a = 0
        num_b = 0
        if index < l1:
            num_a = num1[l1-index-1]
        if index < l2:
            num_b = num2[l2-index-1]
        sum = num_a + num_b + temp
        temp = 0
        if sum > 9:
            sum = sum - 10
            temp = 1

        newNode = ListNode(sum)
        if head == None:
            head = newNode
        else:
            newNode.next = head
            head = newNode
        index += 1

    if temp != 0:
        newNode = ListNode(temp)
        if head == None:
            head = newNode
        else:
            newNode.next = head
            head = newNode
    return head


# NodeList 1
head1 = ListNode(7)
node2 = ListNode(2)
node3 = ListNode(4)
node4 = ListNode(3)

head1.next = node2
node2.next = node3
node3.next = node4

# NodeList 2
head2 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)

head2.next = node5
node5.next = node6


result = addTwoNumbers(head1, head2)
print("result: ")
printNodeList(result)

