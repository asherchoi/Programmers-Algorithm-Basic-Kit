
def solution(board):
    x, y = len(board[0]), len(board)
    if not sum([sum(b) for b in board]):
        return 0
    largest = 1
    for j in range(y):
        for i in range(x):
            if i and j and board[j][i]:
                board[j][i] = min(board[j-1][i], board[j-1][i-1], board[j][i-1]) + 1
                if board[j][i] > largest:
                    largest = board[j][i]
    return largest**2


print(solution([[0,1,1,1],
                [1,1,1,1],
                [1,1,1,1],
                [0,0,1,0]])) # 9

print(solution([[0,0,1,1],
                [1,1,1,1]]))  # 4
                
print(solution([[0, 0],
                [0, 1]]))  # 1

print(solution([[1,1,1,1],
                [0,1,1,1],
                [0,1,1,1]]))  # 9

print(solution([[0], [1]]))  # 1

