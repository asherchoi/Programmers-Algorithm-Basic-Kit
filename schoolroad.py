
def solution(m, n, puddles):
    mem = [[0]*(m+1) for _ in range(n+1)]
    mem[1][1] = 1
    for x in range(1, m+1):
        for y in range(1, n+1):
            if (x, y) == (1, 1):
                continue
            if [x, y] in puddles:
                mem[y][x] = 0
            else:
                mem[y][x] = mem[y-1][x] + mem[y][x-1]
    return mem[-1][-1] % 1000000007


print(solution(4, 3, [[2, 2]]))  # 4