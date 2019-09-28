


def totalScoreOfValidMove(N, M, scores, labels):
    total_score = 0
    for i in range(0, N):
        target = i + 2
        while target < N:
            if labels[i] == labels[target]:
                score = (i + target + 2) * (scores[i] + scores[target])
                total_score += score
            target += 2
    return total_score

N1 = 5
M1 = 2
scores = [1, 2, 3, 4, 5]
labels = [1, 2, 1, 2, 1]

#print(totalScoreOfValidMove(N1, M1, scores, labels))

import sys
if __name__ == "__main__":
    # 读取第一行的n
    n1 = sys.stdin.readline().strip()
    line1 = str(n1).split(" ")
    N = int(line1[0])
    M = int(line1[1])

    n2 = sys.stdin.readline().strip()
    line2 = str(n2).split(" ")
    scores = list()
    for i in range(len(line2)):
        scores.append(int(line2[i]))

    n3 = sys.stdin.readline().strip()
    line3 = str(n3).split(" ")
    labels = list()
    for i in range(len(line3)):
        labels.append(int(line3[i]))
    print(totalScoreOfValidMove(N, M, scores, labels))
