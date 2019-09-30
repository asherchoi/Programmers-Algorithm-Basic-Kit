
def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if not n % i:
            return False
    return True


def solution(nums):
    from itertools import combinations
    count = 0
    for com in combinations(nums, 3):
        if is_prime(sum(com)):
            count += 1
    return count


print(solution([1,2,3,4]))  #	1
print(solution([1,2,7,6,4]))  # 4