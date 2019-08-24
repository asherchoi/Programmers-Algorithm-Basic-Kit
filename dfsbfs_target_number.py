
def solution1(numbers, target):
    cnt = 0

    def dfs(cur_sum=0, idx=0):
        if idx == len(numbers):
            if cur_sum == target:
                nonlocal cnt
                cnt += 1
        else:
            dfs(cur_sum+numbers[idx], idx+1)
            dfs(cur_sum-numbers[idx], idx+1)

    dfs(0, 0)
    return cnt


def solution2(numbers, target):
    cnt = 0
    stack = [(0, 0)]

    while stack:
        cur_sum, idx = stack.pop()
        if idx == len(numbers):
            if cur_sum == target:
                cnt += 1
        else:
            stack.append((cur_sum + numbers[idx], idx + 1))
            stack.append((cur_sum - numbers[idx], idx + 1))

    return cnt


print(solution2([1, 1, 1, 1, 1], 3))	#5
print(solution2([1, 2, 3, 4, 5], 3)) #?
