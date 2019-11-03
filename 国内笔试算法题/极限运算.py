

def function(n, m, a, b):
    i = 1
    result = None
    last = None
    diff = None
    while diff != 0:
        fx = f(i, n, a)
        gx = f(i, m, b)

        if fx / gx == 0:
            temp_string = "0/1"
        else:
            max_common_factor = maxCommonFactor(fx, gx)
            fx //= max_common_factor
            gx //= max_common_factor
            temp_string = str(abs(fx)) + '/' + str(abs(gx))
            if fx < 0 or gx < 0:
                temp_string = "-" + temp_string

        if last == None:
            last = fx / gx
            result = temp_string

        else:
            new_diff = fx / gx - last
            last = fx / gx

            if diff == None:
                diff = new_diff
            else:
                if new_diff > diff:
                    result = "1/0"
                    break
                elif new_diff == diff:
                    if new_diff == 0:
                        break
                else:
                    result = temp_string
        i += 1

    return result



def f(x, n, a):
    sum = 0
    for i in range(n):
        sum += a[i] * x ** n
    return sum

def maxCommonFactor(num1, num2):
    factor1 = set()
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            factor1.add(i)
    factor2 = set()
    for i in range(1, num2 + 1):
        if num2 % i == 0:
            factor2.add(i)
    common = sorted(list(factor1 & factor2))
    return common[-1]
n = 2
m = 2
a = [-1, 11]
b = [4, 10]

print(function(n, m, a, b))
