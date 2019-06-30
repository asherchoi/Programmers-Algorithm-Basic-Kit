

def solution(citations):
    citations.sort()
    H = 0
    for h in reversed(range(len(citations))):
        if h+1 <= len([n for n in citations if n >= h+1]):
            H = h+1
            break
    return H


print(solution([3, 0, 6, 1, 5]))
print(solution([22, 42])) #:2
print(solution([3, 3, 3, 4, 4, 0, 6, 1, 5]))
