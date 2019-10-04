"""
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
    Input:
    letters = ["c", "f", "j"]
    target = "a"
    Output: "c"

    Input:
    letters = ["c", "f", "j"]
    target = "c"
    Output: "f"

    Input:
    letters = ["c", "f", "j"]
    target = "d"
    Output: "f"

    Input:
    letters = ["c", "f", "j"]
    target = "g"
    Output: "j"

    Input:
    letters = ["c", "f", "j"]
    target = "j"
    Output: "c"

    Input:
    letters = ["c", "f", "j"]
    target = "k"
    Output: "c"
Note:
    letters has a length in range [2, 10000].
    letters consists of lowercase letters, and contains at least 2 unique letters.
    target is a lowercase letter.
"""

def nextGreatestLetter(letters, target):
    # get the ascii value of the target letter
    target_index = ord(target)
    # record the closest letter and the min distance
    closest_char = None
    min_distance = 0
    # iterate over the letters list
    for letter in letters:
        # get the ascii value of the letter
        letter_index = ord(letter)
        # compare the letter and the target, calculate the distance
        if target_index < letter_index:
            d = letter_index - target_index
        elif target_index > letter_index:
            d = (letter_index + 26) - target_index
        else:
            # if they are equal, skip it
            continue
        # update the min distance and the closest letter
        if closest_char == None:
            min_distance = d
            closest_char = letter
        else:
            if d < min_distance:
                closest_char = letter
                min_distance = d
    return closest_char

letters1 = ["c", "f", "j"]
target1 = "a"

letters2 = ["c", "f", "j"]
target2 = "c"

letters3 = ["c", "f", "j"]
target3 = "d"

letters4 = ["c", "f", "j"]
target4 = "g"

letters5 = ["c", "f", "j"]
target5 = "j"

letters6 = ["c", "f", "j"]
target6 = "k"

print(nextGreatestLetter(letters6, target6))
