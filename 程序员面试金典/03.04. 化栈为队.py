"""
实现一个MyQueue类，该类用两个栈来实现一个队列。

示例：
    MyQueue queue = new MyQueue();

    queue.push(1);
    queue.push(2);
    queue.peek();  // 返回 1
    queue.pop();   // 返回 1
    queue.empty(); // 返回 false

说明：
    你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size 和 is empty 操作是合法的。
    你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
    假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-queue-using-stacks-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        """
        Initialize your data structure here.
        """


    def push(self, x):
        l = len(self.stack1)
        while l != 0:
            # stack2.push(stack1.pop())
            self.stack2.append(self.stack1[-1])
            del self.stack1[-1]
            l -= 1
        # stack1.push()
        self.stack1.append(x)
        l = len(self.stack2)
        while l != 0:
            # stack1.push(stack2.pop())
            self.stack1.append(self.stack2[-1])
            del self.stack2[-1]
            l -= 1
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """


    def pop(self):
        l = len(self.stack1)
        if l == 0:
            return None

        # stack1.pop()
        top = self.stack1[-1]
        del self.stack1[-1]
        return top
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """


    def peek(self):
        l = len(self.stack1)
        if l == 0:
            return None

        # stack1.pop()
        top = self.stack1[-1]
        return top
        """
        Get the front element.
        :rtype: int
        """


    def empty(self):
        if len(self.stack1) == 0:
            return True
        else:
            return False
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
queue = MyQueue()

queue.push(1)
queue.push(2)
print(queue.peek())  # 返回 1
print(queue.pop())   # 返回 1
print(queue.empty())# 返回 false
