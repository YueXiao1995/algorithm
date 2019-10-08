"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> Returns -3.
    minStack.pop();
    minStack.top();      --> Returns 0.
    minStack.getMin();   --> Returns -2.
"""


class MinStack(object):

    def __init__(self):
        self.data = list()

    def push(self, x):
        self.data += [x]

    def pop(self):
        if len(self.data) > 0:
            del self.data[-1]

    def top(self):
        if len(self.data) > 0:
            return self.data[-1]
        else:
            return None

    def getMin(self):
        if len(self.data) > 0:
            return min(self.data)
        else:
            return None

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
obj.pop()
obj.pop()
obj.pop()
print(obj.getMin())
