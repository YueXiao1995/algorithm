"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.

Example:
    MyStack stack = new MyStack();
    stack.push(1);
    stack.push(2);
    stack.top();   // returns 2
    stack.pop();   // returns 2
    stack.empty(); // returns false

Notes:
    You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
    Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
    You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
"""


class MyStack(object):
    def __init__(self):
        self.queue_1 = list()
        self.top_value = None

    def push(self, x):
        self.queue_1.append(x)
        self.top_value = x

    def pop(self):
        queue_2 = list()
        for i in range(len(self.queue_1) - 1):
            self.top_value = self.queue_1.pop(0)
            queue_2.append(self.top_value)
        return_value = self.queue_1.pop(0)
        self.queue_1 = queue_2
        return return_value

    def top(self):
        return self.top_value

    def empty(self):
        if len(self.queue_1) == 0:
            return True
        else:
            return False

obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.pop())
print(obj.top())
print(obj.empty())
