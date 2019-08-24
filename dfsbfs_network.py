
class Network(object):
    def __init__(self, n, adj_matrix):
        self.n = n
        self.visited = [0] * n
        self.adj_matrix = adj_matrix

    def count(self):
        count = 0
        for i in range(self.n):
            if not self.visited[i]:
                self.dfs(i)
                count += 1
        return count

    def dfs(self, i):
        self.visited[i] = 1
        for j in range(self.n):
            if not self.visited[j] and self.adj_matrix[i][j]:
                self.dfs(j)


def solution(n, computers):
    network = Network(n, computers)
    return network.count()


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