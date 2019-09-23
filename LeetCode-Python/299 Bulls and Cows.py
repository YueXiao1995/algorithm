"""
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows.

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:
    Input: secret = "1807", guess = "7810"
    Output: "1A3B"
    Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
    Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
"""


def getHint(secret, guess):
    # convert the strings to lists
    secret = list(secret)
    guess = list(guess)

    # count the bulls, and delete the numbers in these positions from the lists
    bulls = 0
    l = len(secret)
    i = 0
    while i < l:
        if secret[i] == guess[i]:
            bulls += 1
            del secret[i]
            del guess[i]
            l -= 1
            continue
        i += 1

    # count the freq of each num in remained secret list
    num_freq_secret = dict()
    for num in secret:
        if num in num_freq_secret:
            num_freq_secret[num] += 1
        else:
            num_freq_secret[num] = 1

    # count the freq of each num in remained guess list
    num_freq_guess = dict()
    for num in guess:
        if num in num_freq_guess:
            num_freq_guess[num] += 1
        else:
            num_freq_guess[num] = 1

    # count the cows
    cows = 0
    # iterate the freq dict of the guess
    for num in num_freq_guess:
        # check if this key exist in the freq dict of the secret
        if num in num_freq_secret:
            # find the minimum freq of a num in these two dicts, add it to cows
            if num_freq_guess[num] < num_freq_secret[num]:
                cows += num_freq_guess[num]
            else:
                cows += num_freq_secret[num]
    # form a string and return
    return str(bulls) + "A" + str(cows) + "B"

secret1 = "1807"
guess1 = "7810"

secret2 = "1123"
guess2 = "0111"

print(getHint(secret2, guess2))
