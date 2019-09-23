"""
# get the input
input_value = list()
while 1:
    a = []
    s = input()
    if s != "":
        for x in s.split():
            a.append(int(x))
        input_value.append(a)
    else:
        break

print(input_value)

# method
def f(input_value):
    out_put = list()
    for row in input_value:
        sum = 0
        for num in row:
            sum += num
        out_put.append(sum)

    return out_put

result =  f(input_value)

# print out the result
for num in result:
    print(num)
"""

def f(S, T):
    num_of_t_in_s = 0
    result = list()
    l = len(T)
    for i in range(len(S)):
        if i >= l-1:
            if S[i-l+1:i+1] == T:
                num_of_t_in_s += 1
        result.append(str(num_of_t_in_s))
    #result = (" ").join(result)
    return result

input_value = list()
while 1:
    s = input()
    if s != "":
        input_value.append(s)
    else:
        break
S = input_value[0]
T = input_value[1]

#S = "a"
#T = "a"

result = (f(S, T))

print(str(result).replace(', ', ' ').replace('\'', '')[1:-1]+' ')


