

def solution(n):
    from collections import deque
    ans = deque()
    while n:
        q, r = divmod(n, 3)
        if not r:
            r = 4
            q -= 1
        ans.appendleft(str(r))
        n = q
    return ''.join(ans)


for n in range(1, 20):
    print(n, solution(n))

