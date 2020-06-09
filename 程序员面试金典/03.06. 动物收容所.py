"""
动物收容所。有家动物收容所只收容狗与猫，且严格遵守“先进先出”的原则。在收养该收容所的动物时，收养人只能收养所有动物中“最老”（由其进入收容所的时间长短而定）的动物，或者可以挑选猫或狗（同时必须收养此类动物中“最老”的）。换言之，收养人不能自由挑选想收养的对象。请创建适用于这个系统的数据结构，实现各种操作方法，比如enqueue、dequeueAny、dequeueDog和dequeueCat。允许使用Java内置的LinkedList数据结构。

enqueue方法有一个animal参数，animal[0]代表动物编号，animal[1]代表动物种类，其中 0 代表猫，1 代表狗。

dequeue*方法返回一个列表[动物编号, 动物种类]，若没有可以收养的动物，则返回[-1,-1]。

示例1:
     输入：
    ["AnimalShelf", "enqueue", "enqueue", "dequeueCat", "dequeueDog", "dequeueAny"]
    [[], [[0, 0]], [[1, 0]], [], [], []]
     输出：
    [null,null,null,[0,0],[-1,-1],[1,0]]

示例2:
     输入：
    ["AnimalShelf", "enqueue", "enqueue", "enqueue", "dequeueDog", "dequeueCat", "dequeueAny"]
    [[], [[0, 0]], [[1, 0]], [[2, 1]], [], [], []]
     输出：
    [null,null,null,null,[2,1],[0,0],[1,0]]

说明:
    收纳所的最大容量为20000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/animal-shelter-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class AnimalShelf(object):

    def __init__(self):
        self.animals = []
        self.temp = []

    def enqueue(self, animal):
        # animals.add(animal)
        self.animals.append(animal)
        """
        :type animal: List[int]
        :rtype: None
        """


    def dequeueAny(self):
        if len(self.animals) == 0:
            return [-1, -1]
        # animals.remove()
        animal = self.animals[0]
        del self.animals[0]
        return animal
        """
        :rtype: List[int]
        """


    def dequeueDog(self):
        if len(self.animals) == 0:
            return [-1, -1]

        l = len(self.animals)
        oldest_dog = None
        while l != 0:
            # temp.add(animals.remove())
            if self.animals[0][1] == 1 and oldest_dog == None:
                oldest_dog = self.animals[0]
            else:
                self.temp.append(self.animals[0])
            del self.animals[0]
            l -= 1

        l = len(self.temp)
        while l != 0:
            # animals.add(temp.remove())
            self.animals.append(self.temp[0])
            del self.temp[0]
            l -= 1
        if oldest_dog != None:
            return oldest_dog
        else:
            return [-1, -1]

        """
        :rtype: List[int]
        """


    def dequeueCat(self):
        if len(self.animals) == 0:
            return [-1, -1]

        l = len(self.animals)
        oldest_cat = None
        while l != 0:
            # temp.add(animals.remove())
            if self.animals[0][1] == 0 and oldest_cat == None:
                oldest_cat = self.animals[0]
            else:
                self.temp.append(self.animals[0])
            del self.animals[0]
            l -= 1

        l = len(self.temp)
        while l != 0:
            # animals.add(temp.remove())
            self.animals.append(self.temp[0])
            del self.temp[0]
            l -= 1

        if oldest_cat != None:
            return oldest_cat
        else:
            return [-1, -1]
        """
        :rtype: List[int]
        """

def experiment(operations, parameters):
    obj = AnimalShelf()
    result = [None]
    for i in range(1, len(operations)):
        if operations[i] == 'enqueue':
            result.append(obj.enqueue(parameters[i][0]))
        elif operations[i] == 'dequeueCat':
            result.append(obj.dequeueCat())
        elif operations[i] == 'dequeueAny':
            result.append(obj.dequeueAny())
        elif operations[i] == 'dequeueDog':
            result.append(obj.dequeueDog())
    return result

operations = ["AnimalShelf", "enqueue", "enqueue", "dequeueCat", "dequeueDog", "dequeueAny"]
parameters = [[], [[0, 0]], [[1, 0]], [], [], []]
print(experiment(operations, parameters))

operations = ["AnimalShelf", "enqueue", "enqueue", "enqueue", "dequeueDog", "dequeueCat", "dequeueAny"]
parameters = [[], [[0, 0]], [[1, 0]], [[2, 1]], [], [], []]
print(experiment(operations, parameters))
