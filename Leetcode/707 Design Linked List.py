"""
Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next
is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev
to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        return

class MyLindedList(object):
    def __init__(self):
        self.head = None

    def get(self, index):
        val = -1
        i = 0
        head = self.head
        while head:
            if i == index:
                val = head.val
                break
            else:
                head = head.next
                i += 1
        return val

    def addAtHead(self, val):
        if self.get(0) != -1:
            newHead = ListNode(val)
            newHead.next = self.head
            self.head = newHead
        else:
            newHead = ListNode(val)
            self.head = newHead

    def addAtTail(self, val):
        newTail = ListNode(val)
        head = self.head
        while head:
            #print(head.val)
            if head.next == None:
                head.next = newTail
                break
            head = head.next


    def addAtIndex(self, index, val):
        newNode = ListNode(val)
        head = self.head
        nodelist = list()
        len = 0
        while head:
            nodelist.append(head)
            head = head.next
            len += 1

        if index <= len:
            if len > 0: # check if the list is empty
                if index > 0: # check if the index is 0
                    newNode.next = nodelist[index-1].next
                    nodelist[index-1].next = newNode
                else: # add to the head
                    newNode.next = self.head
                    self.head = newNode
            else:
                self.head = newNode

    def deleteAtIndex(self, index):
        head = self.head
        len = 0
        nodelist = list()
        while head:
            nodelist.append(head)
            head = head.next
            len += 1

        if index < len and index >= 0:
            if len > 1:
                if index == 0:
                    self.head = nodelist[index+1]
                elif index < len:
                    nodelist[index-1].next = nodelist[index].next
                elif index == len:
                    nodelist[index-1] = None
            else:
                self.head = None

object = MyLindedList()
object.addAtHead(1)


def printNodeList(node):
    while node:
        print(node.val)
        node = node.next

object = MyLindedList()
object.addAtIndex(0, 10)
#printNodeList(object.head)
object.addAtIndex(0, 20)
printNodeList(object.head)
object.addAtIndex(1,30)
printNodeList(object.head)
print(object.get(0))
