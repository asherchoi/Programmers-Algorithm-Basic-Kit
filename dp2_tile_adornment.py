

def solution(n):
    fib = [1,]*n
    for i in range(2, len(fib)):
        fib[i] = fib[i-1] + fib[i-2]
    return 2*(2*fib[-1]+fib[-2])


print(solution(5))
print(solution(6))
