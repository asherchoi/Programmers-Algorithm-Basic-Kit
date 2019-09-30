

def solution(seq):
    result = []
    for c in seq:
        print(result, c)
        if not result or result[-1] != c:
            result.append(c)
        else:
            result.pop()
    return 0 if result else 1


print(solution("baabaa"))  # 1
print(solution("cdcd")) # 0
print(solution("c")) # 0
