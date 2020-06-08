"""
三合一。描述如何只用一个数组来实现三个栈。

你应该实现push(stackNum, value)、pop(stackNum)、isEmpty(stackNum)、peek(stackNum)方法。stackNum表示栈下标，value表示压入的值。

构造函数会传入一个stackSize参数，代表每个栈的大小。

示例1:
     输入：
    ["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"]
    [[1], [0, 1], [0, 2], [0], [0], [0], [0]]
     输出：
    [null, null, null, 1, -1, -1, true]
    说明：当栈为空时`pop, peek`返回-1，当栈满时`push`不压入元素。

示例2:
     输入：
    ["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"]
    [[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]]
     输出：
    [null, null, null, null, 2, 1, -1, -1]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/three-in-one-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class TripleInOne(object):

    def __init__(self, stackSize):
        self.stackSize = stackSize
        self.sizes = [0, 0, 0]
        self.stack = []

    def push(self, stackNum, value):
        if self.sizes[stackNum] < self.stackSize:
            self.stack.insert(sum(self.sizes[:stackNum + 1]), value)
            self.sizes[stackNum] += 1

    def pop(self, stackNum):
        if self.sizes[stackNum] > 0:
            peek = self.stack[sum(self.sizes[:stackNum + 1]) - 1]
            del self.stack[sum(self.sizes[:stackNum + 1]) - 1]
            self.sizes[stackNum] -= 1
            return peek
        else:
            return -1

    def peek(self, stackNum):
        if self.sizes[stackNum] > 0:
            peek = self.stack[sum(self.sizes[:stackNum + 1]) - 1]
            return peek
        else:
            return -1

    def isEmpty(self, stackNum):
        if self.sizes[stackNum] == 0:
            return True
        else:
            return False




def experiment(operations, parameters):
    obj = TripleInOne(parameters[0][0])
    result = [None]
    for i in range(1, len(operations)):
        if operations[i] == 'push':
            result.append(obj.push(parameters[i][0], parameters[i][1]))
        elif operations[i] == 'pop':
            result.append(obj.pop(parameters[i][0]))
        elif operations[i] == 'peek':
            result.append(obj.peek(parameters[i][0]))
        else:
            result.append(obj.isEmpty(parameters[i][0]))
    return result

operations = ["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"]
parameters = [[1], [0, 1], [0, 2], [0], [0], [0], [0]]
print(experiment(operations, parameters))

operations = ["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"]
parameters = [[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]]
print(experiment(operations, parameters))

operations = ["TripleInOne", "peek", "pop", "isEmpty", "push", "pop", "push", "push", "pop", "push", "push", "isEmpty", "pop", "peek", "push", "peek", "isEmpty", "peek", "pop", "push", "isEmpty", "pop", "peek", "peek", "pop", "peek", "isEmpty", "pop", "push", "isEmpty", "peek", "push", "peek", "isEmpty", "isEmpty", "isEmpty", "isEmpty", "peek", "push", "push", "peek", "isEmpty", "peek", "isEmpty", "push", "push", "push", "peek", "peek", "pop", "push", "push", "isEmpty", "peek", "pop", "push", "peek", "peek", "pop", "isEmpty", "pop", "peek", "peek", "push", "push"]
parameters = [[18], [1], [2], [1], [2, 40], [2], [0, 44], [1, 40], [0], [1, 54], [0, 42], [0], [1], [1], [0, 56], [2], [0], [2], [2], [1, 15], [1], [1], [0], [2], [0], [0], [1], [0], [0, 32], [0], [0], [0, 30], [2], [1], [1], [0], [0], [0], [0, 56], [1, 40], [2], [0], [0], [0], [2, 11], [0, 16], [0, 3], [2], [0], [2], [0, 39], [0, 63], [1], [2], [0], [2, 36], [1], [0], [2], [1], [0], [1], [2], [0, 8], [0, 38]]
print(experiment(operations, parameters))
