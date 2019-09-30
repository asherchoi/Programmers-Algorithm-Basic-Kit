
def solution(m1, m2):
    len_y, len_x = len(m1), len(m2[0])
    m = [[0]*len_x for _ in range(len_y)]
    for i in range(len_y):
        for j in range(len_x):
            m[i][j] = sum([x*y for x, y in zip(m1[i], [k[j] for k in m2])])
    return m


print(solution([[1, 4],
                [3, 2],
                [4, 1]], [[3, 3],
                          [3, 3]])) #[[15, 15],
                                    # [15, 15],
                                    # [15, 15]]
print(solution([[2, 3, 2],
                [4, 2, 4],
                [3, 1, 4]], [[5, 4, 3],
                             [2, 4, 1],
                             [3, 1, 1]])) #	[[22, 22, 11],
                                           # [36, 28, 18],
                                           # [29, 20, 14]]