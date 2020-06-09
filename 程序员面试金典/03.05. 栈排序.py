"""
栈排序。 编写程序，对栈进行排序使最小元素位于栈顶。最多只能使用一个其他的临时栈存放数据，但不得将元素复制到别的数据结构（如数组）中。该栈支持如下操作：push、pop、peek 和 isEmpty。当栈为空时，peek 返回 -1。

示例1:
     输入：
    ["SortedStack", "push", "push", "peek", "pop", "peek"]
    [[], [1], [2], [], [], []]
     输出：
    [null,null,null,1,null,2]

示例2:
     输入：
    ["SortedStack", "pop", "pop", "push", "pop", "isEmpty"]
    [[], [], [], [1], [], []]
     输出：
    [null,null,null,null,null,true]

说明:
    栈中的元素数目在[0, 5000]范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-of-stacks-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class SortedStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        l = len(self.stack)
        temp = []
        if l == 0:
            self.stack.append(val)
        else:
            is_pushed = None
            while l != 0:
                if is_pushed == None and self.stack[-1] > val:
                    # temp.push()
                    temp.append(val)
                    is_pushed = False
                # temp.push(stack.pop())
                temp.append(self.stack[-1])
                del self.stack[-1]
                l -= 1
            # if all of the num in stack is smaller than val
            if is_pushed == None:
                temp.append(val)
            l = len(temp)
            while l != 0:
                # stack.push(temp.pop())
                self.stack.append(temp[-1])
                del temp[-1]
                l -= 1
        """
        :type val: int
        :rtype: None
        """


    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            top = self.stack[-1]
            del self.stack[-1]
            return top

        """
        :rtype: None
        """


    def peek(self):
        if len(self.stack) == 0:
            return -1
        else:
            top = self.stack[-1]
            return top
        """
        :rtype: int
        """


    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
        """
        :rtype: bool

       """
def experiment(operations, parameters):
    obj = SortedStack()
    result = [None]
    for i in range(1, len(operations)):
        if operations[i] == 'push':
            result.append(obj.push(parameters[i][0]))
        elif operations[i] == 'pop':
            result.append(obj.pop())
        elif operations[i] == 'peek':
            result.append(obj.peek())
        elif operations[i] == 'isEmpty':
            result.append(obj.isEmpty())
    return result

operations =["SortedStack", "push", "push", "peek", "pop", "peek"]
parameters = [[], [1], [2], [], [], []]
print(experiment(operations, parameters))

operations = ["SortedStack", "pop", "pop", "push", "pop", "isEmpty"]
parameters = [[], [], [], [1], [], []]
print(experiment(operations, parameters))
