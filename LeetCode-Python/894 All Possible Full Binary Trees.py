"""
A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.

Example 1:
    Input: 7
    Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]

    Explanation:

Note:
    1 <= N <= 20
"""

nums = [3, 2, 5, 23, 24, 4, 6, 9, 11, 43]


# 构建大顶堆
def buildMaxHeap(nums):
    # 堆的前len(nums)//2个节点会有子叶，所以只需要考虑它们, 从后往前进行历遍
    for i in range((len(nums) // 2), -1, -1):
        heapify(nums, i)


# 递归地比较节点与子叶的值，如果子叶大于节点，则进行交换
def heapify(nums, i):
    # 算出两个子叶的位置
    left = 2 * i + 1
    right = 2 * i + 2
    # 假设节点就是最大值
    largest = i
    # 首先判断这两个子叶在不在堆中，然后比较与根节点的大小
    if left < len(nums) and nums[left] > nums[largest]:
        largest = left
    if right < len(nums) and nums[right] > nums[largest]:
        largest = right
    # 判断最初的堆顶是否为最大值，如果是，则什么都不做
    if largest != i:
        # 如果不是，此时nums[largest]必为最大，与nums[i]对调，并递归地检查下一层
        swap(nums, largest, i)
        heapify(nums, largest)


# 交换list中两个元素的位置
def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


def heapSort(nums):
    # 从堆底到堆顶（即数组的最后一位到第一位），通过与子叶比较大小，并交换的方式，得到大顶堆
    # 最后一层的节点由于没有子叶， 所以不用参与比较，因此有子叶，也就是有需要进行比较的节点
    # 数目就 len(nums) // 2
    buildMaxHeap(nums)
    # 初始化排序完成部分的大小
    i = 0
    while i < len(nums):
        # 将堆顶(nums[0])与堆尾(nums[i])进行互换，堆的大小 - 1， nums[i]归入已排序部分
        swap(nums, 0, len(nums) - i - 1)
        i += 1
        # 从新堆顶开始，递归地比较子节点与其子叶的大小并互换，让堆重新成为大顶堆
        heapify(nums[:len(nums) - i], 0)
    return nums


print('Before:')
print(nums)
nums = heapSort(nums)
print('After:')
print(nums)
