
def solution(number, k):
    answer = [number[0]]
    for n in number[1:]:
        while answer and answer[-1] < n and k > 0:
            answer.pop()
            k -= 1
        answer.append(n)
    if k > 0:
        answer = answer[:-k]
    return ''.join(answer)
        
print(solution("1231234", 3)) #3234
print(solution("1924", 3)) #9
print(solution("4177252841", 4)) #775841
print(solution("10000", 2)) #100
print(solution("1924", 2)) #94

