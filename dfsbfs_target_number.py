
def solution1(numbers, target):
    count = 0
    def dfs(sum, i):
        if i == len(numbers):
            if sum == target:
                nonlocal count
                count += 1
        else:
            dfs(sum+numbers[i], i+1)
            dfs(sum-numbers[i], i+1)
    dfs(0, 0) # sum, index
    return count


def solution2(numbers, target):
    count = 0
    stack = [(0, 0)]
    while stack:
        sum, i = stack.pop()
        if i == len(numbers):
            if sum == target:
                count += 1
        else:
            stack.append((sum+numbers[i], i+1))
            stack.append((sum-numbers[i], i+1))
    return count

print(solution2([1, 1, 1, 1, 1], 3))	#5
print(solution2([1, 2, 3, 4, 5], 3)) #?
