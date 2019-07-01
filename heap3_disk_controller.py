
from heapq import heapify, heappop

def solution(jobs):
    cur_time, jobs_len = 0, len(jobs)
    ttl = []
    while jobs:
        preemptive = [list(reversed(j)) for j in jobs if j[0] <= cur_time]
        if not preemptive:
            cur_time += 1 
            continue
        heapify(preemptive)
        preempt = list(reversed(heappop(preemptive)))
        ttl.append(preempt[1] - preempt[0] + cur_time)
        jobs.remove(preempt)
        cur_time += preempt[1]
    return sum(ttl)//jobs_len
        
    
print(solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]])) #13
print(solution([[0, 3], [1, 9], [2, 6]])) #9
print(solution([[0, 5], [1, 2], [5, 5]])) #6

