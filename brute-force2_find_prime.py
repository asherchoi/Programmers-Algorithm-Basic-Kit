from itertools import permutations


def solution(numbers):
    nums = list(numbers)
    sequences = set()
    for i in range(1, len(nums)+1):
        [sequences.add(int(''.join(x))) for x in permutations(nums, i)]
    print(sequences)
    return len([x for x in sequences if is_prime(x)])


def is_prime(n):
    answer = False
    if n>1:
        for x in range(2, n):
            if not n%x:
                break
        else:
            answer = True
    return answer


print(solution("0000"))  # 0
print(solution("17"))  # 3
print(solution("011"))  # 2
