"""
堆盘子。设想有一堆盘子，堆太高可能会倒下来。因此，在现实生活中，盘子堆到一定高度时，我们就会另外堆一堆盘子。请实现数据结构SetOfStacks，模拟这种行为。SetOfStacks应该由多个栈组成，并且在前一个栈填满时新建一个栈。此外，SetOfStacks.push()和SetOfStacks.pop()应该与普通栈的操作方法相同（也就是说，pop()返回的值，应该跟只有一个栈时的情况一样）。 进阶：实现一个popAt(int index)方法，根据指定的子栈，执行pop操作。

当某个栈为空时，应当删除该栈。当栈中没有元素或不存在该栈时，pop，popAt 应返回 -1.

示例1:
     输入：
    ["StackOfPlates", "push", "push", "popAt", "pop", "pop"]
    [[1], [1], [2], [1], [], []]
     输出：
    [null, null, null, 2, 1, -1]

示例2:
     输入：
    ["StackOfPlates", "push", "push", "push", "popAt", "popAt", "popAt"]
    [[2], [1], [2], [3], [0], [0], [0]]
     输出：
    [null, null, null, null, 2, 1, 3]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/stack-of-plates-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class StackOfPlates(object):

    def __init__(self, cap):
        self.cap = cap
        self.stack_sizes = []
        self.stacks = []
        """
        :type cap: int
        """

    def push(self, val):
        if self.cap != 0:
            if len(self.stack_sizes) == 0:
                self.stacks.append([val])
                self.stack_sizes.append(1)
            else:
                if self.stack_sizes[-1] < self.cap:
                    self.stacks[-1].append(val)
                    self.stack_sizes[-1] += 1
                else:
                    self.stacks.append([val])
                    self.stack_sizes.append(1)

        """
        :type val: int
        :rtype: None
        """


    def pop(self):
        if len(self.stack_sizes) == 0:
            return -1
        else:
            top = self.stacks[-1][-1]
            if self.stack_sizes[-1] == 1:
                del self.stack_sizes[-1]
                del self.stacks[-1]
            else:
                self.stack_sizes[-1] -= 1
                del self.stacks[-1][-1]
            return top




    def popAt(self, index):
        if len(self.stack_sizes) == 0 or index >= len(self.stack_sizes):
            return -1
        else:
            top = self.stacks[index][-1]
            if self.stack_sizes[index] == 1:
                del self.stack_sizes[index]
                del self.stacks[index]
            else:
                self.stack_sizes[index] -= 1
                del self.stacks[index][-1]
            return top


def experiment(operations, parameters):
    obj = StackOfPlates(parameters[0][0])
    result = [None]
    for i in range(1, len(operations)):
        if operations[i] == 'push':
            result.append(obj.push(parameters[i][0]))
        elif operations[i] == 'pop':
            result.append(obj.pop())
        else:
            result.append(obj.popAt(parameters[i][0]))
    return result

operations = ["StackOfPlates", "push", "push", "popAt", "pop", "pop"]
parameters = [[1], [1], [2], [1], [], []]
print(experiment(operations, parameters))

operations = ["StackOfPlates", "push", "push", "push", "popAt", "popAt", "popAt"]
parameters = [[2], [1], [2], [3], [0], [0], [0]]
print(experiment(operations, parameters))

operations = ["StackOfPlates", "pop", "pop", "popAt", "popAt", "pop", "push", "push", "push", "push", "pop", "push", "push", "popAt", "pop", "popAt", "push", "popAt", "pop", "push", "pop", "pop", "pop", "popAt", "push", "pop", "popAt", "pop", "push", "popAt", "popAt", "push", "popAt", "popAt", "push", "pop", "popAt", "popAt", "popAt", "pop", "popAt", "popAt", "push", "popAt", "push", "push", "pop", "popAt", "popAt", "push", "popAt", "push", "pop", "pop", "push", "push", "push", "popAt", "popAt", "pop", "popAt", "pop", "pop", "push", "push"]
parameters = [[6], [], [], [1], [3], [], [40], [10], [44], [44], [], [24], [42], [4], [], [0], [42], [5], [], [29], [], [], [], [0], [56], [], [4], [], [34], [1], [4], [52], [4], [6], [63], [], [6], [6], [1], [], [6], [2], [47], [1], [45], [52], [], [6], [6], [20], [4], [17], [], [], [43], [6], [30], [2], [3], [], [3], [], [], [51], [46]]
print(experiment(operations, parameters))

operations = ["StackOfPlates", "push", "push", "push", "push", "push", "push", "push", "push", "push", "push", "push", "push", "push", "push", "push", "push", "push", "push", "push", "push", "push", "push", "push", "push", "push", "push", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop"]
parameters = [[0], [2], [8], [56], [1], [39], [40], [44], [63], [11], [38], [20], [55], [25], [14], [11], [1], [20], [16], [6], [18], [3], [39], [45], [2], [22], [64], [6], [30], [39], [3], [19], [63], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
print(experiment(operations, parameters))
