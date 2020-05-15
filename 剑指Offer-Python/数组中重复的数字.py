"""
题目描述
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，
那么对应的输出是第一个重复的数字2
"""


# 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
# 函数返回True/False
def duplicate(numbers, duplication):

    return 0

numbers1 = [2,3,1,0,2,5,3]
duplication = []



def sortListByLastElement(tuples):
    last_element = dict()
    for tuple in tuples:
        if tuple[-1] not in last_element:
            last_element[tuple[-1]] = [tuple]
        else:
            last_element[tuple[-1]].append(tuple)
    print(last_element)
    new_list = list()
    for element in sorted(last_element.keys()):
        print(element)
        new_list.extend(last_element[element])
    return new_list



print(sortListByLastElement([(0, 5), (-1, 2), (4, 4), (2, 3), (3, 1)]))

def removeingFromSpecificIndex(samples, indexs_for_removing):
    for i in range(len(indexs_for_removing)):
        del samples[indexs_for_removing[-i-1]]
    return samples
samples = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
indexs_for_removing = [0, 4, 5]
print(removeingFromSpecificIndex(samples, indexs_for_removing))

import numpy as np
#a = np.array(((2, 3), (3, 5)))
a = np.matrix(((2, 3), (3, 5)))

import numpy.linalg as npl

