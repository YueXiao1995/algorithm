"""
A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types of commands:

-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles.

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from the origin.

Example 1:
    Input: commands = [4,-1,3], obstacles = []
    Output: 25
    Explanation: robot will go to (3, 4)

Example 2:
    Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
    Output: 65
    Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)

Note:
    0 <= commands.length <= 10000
    0 <= obstacles.length <= 10000
    -30000 <= obstacle[i][0] <= 30000
    -30000 <= obstacle[i][1] <= 30000
    The answer is guaranteed to be less than 2 ^ 31.
"""

def robotSim(commands, obstacles):
    # store the obstacles into two dicts,
    # one is using x (obstacle[0]) as the key,
    # the other is using y(obstacle[1]) ase the key
    obstacles_x = dict()
    obstacles_y = dict()
    for obstacle in obstacles:
        if obstacle[0] not in obstacles_x:
            obstacles_x[obstacle[0]] = {obstacle[1]}
        else:
            obstacles_x[obstacle[0]].add(obstacle[1])

        if obstacle[1] not in obstacles_y:
            obstacles_y[obstacle[1]] = {obstacle[0]}
        else:
            obstacles_y[obstacle[1]].add(obstacle[0])

    # N, E, S, W
    move_directions = [[1, 1], [0, 1], [1, -1], [0, -1]]
    direction = 0
    position = [0, 0]
    maximum_distance = 0
    for command in commands:
        # the direction after turn right 90 degrees
        if command == -1:
            direction = (direction + 1) % 4
        # the direction after turn left 90 degrees
        elif command == -2:
            direction = (4 + direction - 1) % 4
        # move forward
        else:
            index = move_directions[direction][0]
            d = move_directions[direction][1]
            # check if the robot is going to move vertically
            if index == 1:
                # check if there is any obstacle in this column
                if position[0] not in obstacles_x:
                    position[index] += d * command
                else:
                    for i in range(command):
                        if (position[index] + d) not in obstacles_x[position[0]]:
                            position[index] += d
                        else:
                            break
            # else the robot is going to move horizontally
            else:
                # check if there is any obstacle in this row
                if position[1] not in obstacles_y:
                    position[index] += d * command
                # else, move until meet the obstacle
                else:
                    for i in range(command):
                        if position[index] + d not in obstacles_y[position[1]]:
                            position[index] += d
                        else:
                            break
        # calculate the square of the Euclidean distance
        distance = position[0] ** 2 + position[1] ** 2
        # update the square of the max Euclidean distance
        if distance > maximum_distance:
            maximum_distance = distance
    return maximum_distance

commands1 = [4,-1,3]
obstacles1 = []

commands2 = [4, -1, 4, -2, 4]
obstacles2 = [[2, 4]]

print(robotSim(commands2, obstacles2))
