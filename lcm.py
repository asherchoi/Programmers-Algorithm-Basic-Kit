

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a, b):
    gcd_value = gcd(a, b)
    if not gcd_value:
        return 0
    return abs((a*b)//gcd_value)


def solution(arr):
    while len(arr) != 1:
        a = arr.pop()
        b = arr.pop()
        arr.append(lcm(a, b))
    return arr[0]


print(solution([2, 6, 8, 14]))  # 168
print(solution([1, 2, 3]))  # 6

