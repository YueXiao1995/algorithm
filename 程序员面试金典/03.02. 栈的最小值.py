"""
请设计一个栈，除了常规栈支持的pop与push函数以外，还支持min函数，该函数返回栈元素中的最小值。执行push、pop和min操作的时间复杂度必须为O(1)。

示例：

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-stack-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = []
        """
        initialize your data structure here.
        """


    def push(self, x):
        self.stack.append(x)
        if len(self.min) == 0:
            self.min.append(x)
        else:
            self.min.append(min(self.min[-1], x))
        """
        :type x: int
        :rtype: None
        """


    def pop(self):
        if len(self.stack) > 0:
            top = self.stack[-1]
            del self.stack[-1]
            del self.min[-1]
            return top
        """
        :rtype: None
        """


    def top(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]


    def getMin(self):
        if len(self.min) != 0:
            return self.min[-1]
        else:
            return None
        """
        :rtype: int
        """

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())
