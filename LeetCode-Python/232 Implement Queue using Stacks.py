"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

Example:
    MyQueue queue = new MyQueue();
    queue.push(1);
    queue.push(2);
    queue.peek();  // returns 1
    queue.pop();   // returns 1
    queue.empty(); // returns false

Notes:
    You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
    Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
    You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""

class MyQueue(object):
    def __init__(self):
        self.stack = list()
        self.peek_value = None

    def push(self, x):
        if len(self.stack) == 0:
            self.peek_value = x
        self.stack.append(x)

    def pop(self):
        temp_stack = list()
        for i in range(len(self.stack) - 1):
            self.peek_value = self.stack.pop(-1)
            temp_stack.append(self.peek_value)
        peek = self.stack.pop(-1)

        for i in range(len(temp_stack)):
            self.stack.append(temp_stack.pop(-1))
        return peek

    def peek(self):
        return self.peek_value

    def empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())
print(queue.pop())
print(queue.empty())

