"""
在观星的时候，一种常用的方式是划出类似于正方形的区域内，确定其中所有星星的坐标。

现在我们在星空（一个无限大的二维平面）上建立坐标系。由于星星很小，我们忽略它的面积，认为每一个星星是一个点，且所有星星的坐标都是整数。

幸运星的定义是这一颗星星在这个平面内，正上，正下，正左，正右都有其他的星星(不一定相邻)。

现在，我们已经将这个正方形的区域取出，并且将他们所在的坐标给你。现在希望你能计算，这个平面内有多少颗幸运星？
"""

# input module
"""
num_of_stars = input()
stars = list()
while 1:
    a = []
    s = input()

    if s != "":
        for x in s.split():
            a.append(int(x))
        stars.append(a)
    else:
        break
print(num_of_stars)
print(stars)
"""


def luckyStars(num, stars):
    # create dict to store the information
    x_dict = dict()
    y_dict = dict()
    for star in stars:
        x = star[0]
        y = star[1]
        if x not in x_dict:
            x_dict[x] = [y]
        else:
            x_dict[x].append(y)
        if y not in y_dict:
            y_dict[y] = [x]
        else:
            y_dict[y].append(x)
    # sort the list in dict
    for x in x_dict:
        x_dict[x] = sorted(x_dict[x])
    for y in y_dict:
        y_dict[y] = sorted(y_dict[y])
    # find the lucky stars
    num_of_lucky_stars = 0
    for star in stars:
        x = star[0]
        y = star[1]
        if len(x_dict[x]) > 2 and len(y_dict[y]) > 2:
            if y > x_dict[x][0] and y < x_dict[x][-1] and x > y_dict[y][0] and x < y_dict[y][-1]:
                print(star)
                num_of_lucky_stars += 1
    return num_of_lucky_stars

# test data
num_of_stars = 8
stars = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 1], [1, 2], [-1, 1], [-1, 2]]
print(luckyStars(num_of_stars, stars))
print(stars)

num_of_stars = input()
stars = list()
while 1:
    a = []
    s = input()
    if s != "":
        for x in s.split():
            a.append(int(x))
        stars.append(a)
    else:
        break

del stars[0]
print(num_of_stars)
print(stars)
