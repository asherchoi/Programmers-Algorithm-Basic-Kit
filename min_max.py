

def solution(s):
    _ = list(map(int, s.split()))
    return str(min(_)) + " " + str(max(_))

print(solution("1 2 3 4	1")) # "1 4"
print(solution("-1 -2 -3 -4	-4")) # "-4 -1"
print(solution("-1 -1 -1 -1")) # "-1 -1"