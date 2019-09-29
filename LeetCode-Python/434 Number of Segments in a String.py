"""
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
"""
def countSegments(s: str) -> int:
    # split the string
    s = s.split(" ")
    # count the number of segments in s list which is not equal to ""
    num_of_segments = 0
    for w in s:
        if w != "":
            num_of_segments += 1
    return num_of_segments

input1 = "Hello, my name is John"
input2 = " asfd asfd"
print(countSegments(input1))
