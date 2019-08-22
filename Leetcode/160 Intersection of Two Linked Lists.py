"""
Write a program to find the node at which the intersection of two singly linked lists begins.

【Example 1】
    Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
    Output: Reference of the node with value = 8
    Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
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

# Intersection c
c1 = ListNode(8)
c2 = ListNode(4)
c3 = ListNode(5)

c1.next = c2
c2.next = c3

# NodeList a
a1 = ListNode(4)
a2 = ListNode(1)

a1.next = a2
a2.next = c1


# NodeList b
b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)

b1.next = b2
b2.next = b3
b3.next = c1
"""
# This method is too slow

def getIntersectionNode(headA, headB):
    NodeList = list()
    intersectionNode = None
    while(headA):
        NodeList.append(headA)
        headA = headA.next
    while(headB):
        if headB not in NodeList:
            headB = headB.next
        else:
            intersectionNode = headB
            break
    return intersectionNode
"""
def getIntersectionNode(headA, headB):
    if headA != None and headB!= None:  # check if the Nodelists are empty
        intersectionNode = None
        nodeList_A = list()
        nodeList_B = list()
        while(headA):
            nodeList_A.append(headA)
            headA = headA.next
        while (headB):
            nodeList_B.append(headB)
            headB = headB.next
        lenA = len(nodeList_A)
        lenB = len(nodeList_B)
        if lenA > lenB:
            for i in range(0, lenB):
                if nodeList_B[i] == nodeList_A[lenA-lenB+i]:
                    intersectionNode = nodeList_B[i]
                    break
        else:
            for i in range(0, lenA):
                if nodeList_A[i] == nodeList_B[lenB-lenA+i]:
                    intersectionNode = nodeList_A[i]
                    break
        return intersectionNode
    else:
        return None

printNodeList(getIntersectionNode(a1, b1))
