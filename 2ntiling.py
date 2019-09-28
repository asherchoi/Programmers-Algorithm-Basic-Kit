

def solution(n):
    dp = [1, 2]
    for i in range(2, n):
        temp = (dp[i - 2] + dp[i - 1]) % 1000000007
        dp.append(temp)
    return dp[-1]


print(solution(4))  # 5