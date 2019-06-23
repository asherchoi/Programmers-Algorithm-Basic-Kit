

def solution(prices):
    answer = []
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j-i)
                break
        else:
            answer.append(j-i)
    return answer

print(solution([1,2,3,2,3])) #[4,3,1,1,0]
