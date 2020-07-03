def targetFreq(nums, target):
    count = 0
    for i in range(len(nums)):
        if nums[i] == target:
            count += 1
    return count


def targetFreq2(nums, target):
    count = 0
    start = 0
    end = len(nums) - 1
    while end >= start:
        mid = (start + end) // 2
        if nums[mid] == target:
            count += 1

            for i in range(1, end - mid):
                if nums[mid + i] == target:
                    count += 1
                if nums[mid + i] > target:
                    break

            for i in range(1, mid - start):
                if nums[mid - i] == target:
                    count += 1
                if nums[mid - i] < target:
                    break
            break
        elif nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
    return count

nums = [1, 2, 3, 3, 4, 5]
target = 3
print(targetFreq2(nums, target))

from binarytree import build

tree = build([2, 3, 4, 5, None, None, 6])

def bfs(tree):
    if tree == None:
        return 0
    sum = 0
    queue = list()
    queue.append(tree)
    while True:
        if len(queue) == 0:
            break
        sum += queue[0].value
        if queue[0].left:
            queue.append(queue[0].left)
        if queue[0].right:
            queue.append(queue[0].right)
        del queue[0]
    return sum
print(tree)
print(bfs(tree))



def BigNumberAdd(num1, num2):
    sum = ''
    extra = 0
    for i in range(max(len(num1), len(num2))):
        num = 0
        num += extra
        if i < len(num1):
            num += int(num1[-i - 1])
        if i < len(num2):
            num += int(num2[-i - 1])
        if num // 10 != 0:
            extra = num // 10
            num = num % 10
        else:
            extra = 0
        sum = str(num) + sum
    if extra != 0:
        sum = str(extra) + sum
    return sum


num1 = "1234567890"
num2 = "2345678900"

print(BigNumberAdd(num1, num2))

print(1234567890 + 2345678900)


a = [1, 4, 2, 5, 6]
b = [2, 3, 4, 5]
t = 5

def findMatchPairs(a, b, t):
    diff = set()
    pairs = list()
    for i in range(len(a)):
        diff.add(t - a[i])
    for i in range(len(b)):
        if b[i] in diff:
            pairs.append([b[i], t - b[i]])
    return pairs

print(findMatchPairs(a, b, t))

a = ([0, 1, 2, 3], 4)
print(a)

a[0][0] = 1
print(a)

a = {'a': 2, 'b': 1}
print(sorted(a))


