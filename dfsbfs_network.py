

def solution(n, computers):
    def dfs(i):
        visit[i] = 1
        for j in range(len(computers)):
            if computers[i][j] and not visit[j]:
                dfs(j)

    visit = [0]*len(computers)
    count = 0
    for i in range(n):
        if not visit[i]:
            count += 1
            dfs(i)

    return count


print("#test case 1")
print(solution(3, [[1, 0, 0],
                   [0, 1, 0],
                   [0, 0, 1]]))  # 3

print("#test case 2")
print(solution(3, [[1, 1, 0],
                   [1, 1, 0],
                   [0, 0, 1]]))  # 2

print("#test case 3")
print(solution(3, [[1, 1, 0],
                   [1, 1, 1],
                   [0, 1, 1]]))  # 1

print("#test case 4")
                   #0, 1, 2, 3, 4, 5
print(solution(6, [[1, 1, 1, 0, 0, 0],    # 0
                   [1, 1, 1, 1, 0, 0],    # 1
                   [1, 1, 1, 1, 0, 0],    # 2
                   [0, 1, 1, 1, 0, 0],    # 3
                   [0, 0, 0, 0, 1, 0],    # 4
                   [0, 0, 0, 0, 0, 1]]))  # 5
# 3

print("#test case 5")
                   #0, 1, 2, 3, 4, 5
print(solution(6, [[1, 1, 1, 1, 0, 0],    # 0
                   [1, 1, 1, 1, 0, 0],    # 1
                   [1, 1, 1, 1, 0, 0],    # 2
                   [1, 1, 1, 1, 0, 0],    # 3
                   [0, 0, 0, 0, 1, 0],    # 4
                   [0, 0, 0, 0, 0, 1]]))  # 5
# 3
