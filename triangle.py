from pprint import pprint

def solution(T):
    for l, layer in enumerate(T):
        if l == 0: continue
        for i in range(len(layer)):
            if i == 0:
                T[l][i] = T[l][i] + T[l - 1][i]
            elif i == len(layer) - 1:
                T[l][i] = T[l][i] + T[l - 1][i - 1]
            else:
                c1 = T[l][i] + T[l - 1][i]
                c2 = T[l][i] + T[l - 1][i - 1]
                T[l][i] = max(c1, c2)
    return max(T[-1])


print(solution([[7],
               [3, 8],
              [8, 1, 0],
             [2, 7, 4, 4],
            [4, 5, 2, 6, 5]]))  # 30
