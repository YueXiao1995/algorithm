"""
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
"""
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

def printListFromTailToHead(listNode):
    node_list = list()
    while listNode.next != None:
        node_list.append(listNode.val)
        listNode = listNode.next
    node_list.reverse()
    return node_list
