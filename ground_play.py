
def solution(land):
    for j in range(1, len(land)):
        for i in range(4):
            land[j][i] += max([x for k, x in enumerate(land[j-1]) if k != i])
    return max(land[-1])


print(solution([[1,2,3,5],
                [5,6,7,8],
                [4,3,2,1]]))  # 16

print(solution([[1,2,5,5],
                [7,6,8,7],
                [4,3,2,1]]))  # 17