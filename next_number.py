
def solution(n):
    one_count = bin(n).count('1')
    while True:
        n += 1
        if bin(n).count('1') == one_count:
            return n



print(solution(78))  #83
print(solution(15))  #23