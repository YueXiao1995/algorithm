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
    max_distance = 0
    occupied_seat = list()

    last_occ_seat = None
    for i in range(0, len(seats)):
        if seats[i] == 1:
            occupied_seat.append(i)
            if last_occ_seat == None:
                l = i
                print("jjj")
            else:
                l = (i - last_occ_seat)//2
            if l > max_distance:
                max_distance = l
            last_occ_seat = i

        if i == len(seats) - 1:
            l = len(seats) - last_occ_seat - 1
            if l > max_distance:
                max_distance = l

    print(occupied_seat)
    return max_distance
input1 = [1,0,0,0,1,0,1]
input2 = [1,0,0,0]
input3 = [0,0,1,0,1,1,1]
input4 = [0, 1]
print(maxDistToClosest(input4))
