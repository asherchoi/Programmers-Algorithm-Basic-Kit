
from heapq import heappush, heappop

def solution(stock, dates, supplies, k):
    count, start, pq = 0, 0, []
    while stock < k: 
        for i in range(start, len(dates)):
            if dates[i] <= stock:
                heappush(pq, -supplies[i])
            else:
                start = i
                break
        else:
            start = i+1
        stock -= heappop(pq)
        count += 1
    return count


print(solution(4, [4,10,15], [10,20,30], 40)) #3
print(solution(4, [4,10,15], [20,5,10], 30)) #2
print(solution(4, [1,2,3,4], [10,40,30,20], 100)) #4

