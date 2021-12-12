def FindPossibleList(Lists):
    q = [[]]
    for i in range(len(Lists)):
        for j in range(len(q)):
            for k in range(len(Lists[i])):
                new_list = q[0] + [Lists[i][k]]
                q.append(new_list)
            del q[0]
    return q

lists = [(1, 3), (6, 3, 4)]
print(FindPossibleList(lists))

print('你好')
