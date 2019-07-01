
# solve the problem within O(log n)

from heapq import heappush, heappop, heapify

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    while not (scoville[0] >= K):
        if len(scoville) == 1: #if can't adjust whole food satisfied with scoville K
            answer = -1
            break
        first = heappop(scoville)
        second = heappop(scoville)
        heappush(scoville, first+(second*2))
        answer += 1
        
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7)) #2
