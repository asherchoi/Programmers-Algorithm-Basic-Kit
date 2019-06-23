


def solution(heights):
    answer = [0,]
    for i in range(1, len(heights)):
        cur = heights[i]
        while i:
            i -= 1
            if heights[i] > cur:
                answer.append(i+1)
                break
        else:
            answer.append(0)
    return answer

print(solution([6,9,5,7,4])) # [0,0,2,2,4]
print(solution([3,9,9,3,5,7,2])) # [0,0,0,3,3,3,6]
print(solution([1,5,3,6,7,6,5])) # [0,0,2,0,0,5,6]
