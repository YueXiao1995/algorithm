"""
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

Return that maximum distance to closest person.

Example 1:
    Input: [1,0,0,0,1,0,1]
    Output: 2
    Explanation:
    If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
    If Alex sits in any other open seat, the closest person has distance 1.
    Thus, the maximum distance to the closest person is 2.

Example 2:
    Input: [1,0,0,0]
    Output: 3
    Explanation:
    If Alex sits in the last seat, the closest person is 3 seats away.
    This is the maximum distance possible, so the answer is 3.

Note:
    1 <= seats.length <= 20000
    seats contains only 0s or 1s, at least one 0, and at least one 1.

"""

# Time Limit Exceeded
"""
def maxDistToClosest(seats):
    max_distance = 0
    # find the empty seats and the seats which have been occupied by a person
    empty_seats = list()
    occupied_seats = list()
    for i in range(0, len(seats)):
        if seats[i] == 0:
            empty_seats.append(i)
        else:
            occupied_seats.append(i)
    print("Empty: " + str(empty_seats))
    print("Person: " + str(occupied_seats))
    # find the maximum distance

    for s in empty_seats:
        print("Empty: "+str(s))
        for i in range(0, len(occupied_seats)):
            print("Person:" + str(occupied_seats[i]))
            print(occupied_seats)
            if occupied_seats[i] > s:
                right_d = occupied_seats[i] - s
                if i == 0:
                    min_d = right_d
                else:
                    left_d = s - occupied_seats[i - 1]
                    if right_d > left_d:
                        min_d = left_d
                    else:
                        min_d = right_d
                # update the max distance
                if min_d > max_distance:
                    max_distance = min_d
                if i != 0:
                    occupied_seats = list(occupied_seats[i - 1:])
                break
            elif i == len(occupied_seats) - 1:
                min_d = s - occupied_seats[i]
                if min_d > max_distance:
                    max_distance = min_d
        print(occupied_seats)
    return max_distance
"""

def maxDistToClosest(seats):
    # variable to record the max distance
    max_distance = 0
    # variable to record the position of last occupied seat
    last_occ_seat = None
    # iterate the seats list
    for i in range(0, len(seats)):
        # if the seat is occupied
        if seats[i] == 1:
            # if it is the first occupied seat, the temporary max distance is i - 0
            if last_occ_seat == None:
                l = i
            # else the temporary max distance is  floor(this seat - last occupied seat / 2)
            else:
                l = (i - last_occ_seat)//2
            # update the max distance
            if l > max_distance:
                max_distance = l
            # update the position of last occupied seat
            last_occ_seat = i
        # if reached the end of seats list but the last seats is not occupied, need to calculate the
        # distance between last occupied seat and the end of the list
        if i == len(seats) - 1:
            l = len(seats) - last_occ_seat - 1
            # update the max distance
            if l > max_distance:
                max_distance = l
    return max_distance
input1 = [1,0,0,0,1,0,1]
input2 = [1,0,0,0]
input3 = [0,0,1,0,1,1,1]
input4 = [0, 1]
print(maxDistToClosest(input4))
