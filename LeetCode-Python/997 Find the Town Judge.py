"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3

Note:

1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N
"""


def findJudge(N, trust):
    if len(trust) == 0:
        return 1

    graph = dict()
    for edge in trust:
        if edge[0] in graph:
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]

    most_trusted_people = None
    for point in graph:
        if most_trusted_people == None:
            most_trusted_people = set(graph[point])
        else:
            most_trusted_people = most_trusted_people & set(graph[point])

    positional_judge = list()
    for people in most_trusted_people:
        if people not in graph:
            positional_judge.append(people)
    if len(positional_judge) == 1:
        return positional_judge[0]
    else:
        return -1

N1 = 2
trust1 = [[1,2]]
print(findJudge(N1, trust1))

N2 = 3
trust2 = [[1,3],[2,3]]
print(findJudge(N2, trust2))

N3 = 3
trust3 = [[1,3],[2,3],[3,1]]
print(findJudge(N3, trust3))

N4 = 3
trust4 = [[1,2],[2,3]]
print(findJudge(N4, trust4))

N5 = 4
trust5 = [[1,3],[1,4],[2,3],[2,4],[4,3]]
print(findJudge(N5, trust5))


N6 = 11
trust6 = [[1,8],[1,3],[2,8],[2,3],[4,8],[4,3],[5,8],[5,3],[6,8],[6,3],[7,8],[7,3],[9,8],[9,3],[11,8],[11,3]]
print(findJudge(N6, trust6))
