from collections import deque

def solution(priorities, location):
    queue = deque(zip(priorities, range(len(priorities))))
    count = 0
    while queue:
        p, l = queue.popleft()
        if len(queue) == 0:
            count += 1
            break
        if p < max((x for x,y in queue)):
            queue.append((p,l))
        else:
            count += 1 
            if l == location:
                break
        
    return count


print(solution([2, 1, 3, 2], 2)) #1
print(solution([1, 1, 1, 1, 1, 9], 5))#5
