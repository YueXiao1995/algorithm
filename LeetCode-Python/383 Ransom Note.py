"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
    You may assume that both strings contain only lowercase letters.

    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false
    canConstruct("aa", "aab") -> true
"""
def canConstruct(ransomNote: str, magazine: str) -> bool:
    # count the freq of the chars in magazine
    freq = dict()
    for char in magazine:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1

    # iterate over the ransomNote string to check if it can be constructed by the char in freq dist
    for char in ransomNote:
        # check if the char is contained by the magazine string
        if char not in freq:
            return False
        else:
            # check if there still some char remain in dict
            if freq[char] == 0:
                return False
            else:
                # reduce the amount of the char in dict
                freq[char] -= 1
    return True

ransomNote1 = "a"
magazine1 = "b"

ransomNote2 = "aa"
magazine2 = "ab"

ransomNote3 = "aa"
magazine3 = "aab"

print(canConstruct(ransomNote3, magazine3))
