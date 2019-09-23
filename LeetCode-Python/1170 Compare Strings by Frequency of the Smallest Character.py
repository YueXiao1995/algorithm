"""
Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.



Example 1:
    Input: queries = ["cbd"], words = ["zaaaz"]
    Output: [1]
    Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").

Example 2:
    Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
    Output: [1,2]
    Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").


Constraints:

1 <= queries.length <= 2000
1 <= words.length <= 2000
1 <= queries[i].length, words[i].length <= 10
queries[i][j], words[i][j] are English lowercase letters.

"""

def numSmallerByFrequency(queries, words):

    f_q_list = list()
    for q in queries:
        characters = sorted(list(q))
        smallest_char = None
        f_q = 0
        for char in characters:
            if smallest_char == None:
                smallest_char = char
                f_q += 1
            else:
                if char == smallest_char:
                    f_q += 1
                else:
                    break
        f_q_list.append(f_q)

    f_w_list = list()
    for w in words:
        characters = sorted(list(w))
        smallest_char = None
        f_w = 0
        for char in characters:
            if smallest_char == None:
                smallest_char = char
                f_w += 1
            else:
                if char == smallest_char:
                    f_w += 1
                else:
                    break
        f_w_list.append(f_w)
    result = list()
    for q in f_q_list:
        num = 0
        for w in f_w_list:
            if q < w:
                num += 1
        result.append(num)
    return result

queries = ["cbd"]
words = ["zaaaz"]

queries2 = ["bbb","cc"]
words2 = ["a","aa","aaa","aaaa"]


print(numSmallerByFrequency(queries2, words2))
