"""
Design a Leaderboard class, which has 3 functions:

addScore(playerId, score): Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
top(K): Return the score sum of the top K players.
reset(playerId): Reset the score of the player with the given id to 0. It is guaranteed that the player was added to the leaderboard before calling this function.
Initially, the leaderboard is empty.

Example 1:
    Input:
        ["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
        [[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
    Output:
        [null,null,null,null,null,null,73,null,null,null,141]

    Explanation:
        Leaderboard leaderboard = new Leaderboard ();
        leaderboard.addScore(1,73);   // leaderboard = [[1,73]];
        leaderboard.addScore(2,56);   // leaderboard = [[1,73],[2,56]];
        leaderboard.addScore(3,39);   // leaderboard = [[1,73],[2,56],[3,39]];
        leaderboard.addScore(4,51);   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
        leaderboard.addScore(5,4);    // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
        leaderboard.top(1);           // returns 73;
        leaderboard.reset(1);         // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
        leaderboard.reset(2);         // leaderboard = [[3,39],[4,51],[5,4]];
        leaderboard.addScore(2,51);   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
        leaderboard.top(3);           // returns 141 = 51 + 51 + 39;

Constraints:
    1 <= playerId, K <= 10000
    It's guaranteed that K is less than or equal to the current number of players.
    1 <= score <= 100
    There will be at most 1000 function calls.
"""


class Leaderboard(object):

    def __init__(self):
        self.player = set()
        self.leaderboard = list()

    def addScore(self, playerId, score):
        if playerId not in self.player:
            self.player.add(playerId)
            is_added = False
            for i in range(len(self.leaderboard)):
                if self.leaderboard[i][1] < score:
                    self.leaderboard.insert(i, [playerId, score])
                    is_added = True
                    break
            if not is_added:
                self.leaderboard.append([playerId, score])
        else:
            new_record = None
            index = 0
            for i in range(len(self.leaderboard)):
                if self.leaderboard[i][0] == playerId:
                    new_record = [playerId, self.leaderboard[i][1] + score]
                    del self.leaderboard[i]
                    index = i
                    break
            is_added = False
            for i in reversed(range(index)):
                if self.leaderboard[i][1] > new_record[1]:
                    self.leaderboard.insert(i + 1, new_record)
                    is_added = True
                    break
            if not is_added:
                self.leaderboard.insert(0, new_record)
        print(self.leaderboard)

        """
        :type playerId: int
        :type score: int
        :rtype: None
        """

    def top(self, K):
        sum = 0
        for record in self.leaderboard[:K]:
            sum += record[1]
        print(sum)
        return sum

    def reset(self, playerId):
        for i in range(len(self.leaderboard)):
            if self.leaderboard[i][0] == playerId:
                del self.leaderboard[i]
                break
        self.leaderboard.append([playerId, 0])
        print(self.leaderboard)
        """
        :type playerId: int
        :rtype: None
        """

def experiment(operations, parameters):
    leaderboard = Leaderboard()
    for i in range(1, len(operations)):
        if operations[i] == "addScore":
            leaderboard.addScore(parameters[i][0], parameters[i][1])
        elif operations[i] == "top":
            leaderboard.top(parameters[i][0])
        elif operations[i] == "reset":
            leaderboard.reset(parameters[i][0])

operations1 = ["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
parameters1 = [[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
operations2 = ["Leaderboard","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","addScore","top","reset","reset","addScore","reset"]
parameters2 = [[],[1,13],[2,93],[3,84],[4,6],[5,89],[6,31],[7,7],[8,1],[9,98],[10,42],[5],[1],[2],[3,76],[4,68],[1],[3],[4],[2,70],[2]]

experiment(operations1, parameters1)
experiment(operations2, parameters2)
