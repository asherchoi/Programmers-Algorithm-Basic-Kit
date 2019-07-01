from heapq import heappush, heappop, heapify

def solution(operations):
    pq = []
    for o in operations:
        if o == 'D 1':
            if pq:
                pq = [-x for x in pq]
                heapify(pq)
                heappop(pq)
                pq = [-x for x in pq]
                heapify(pq)
        elif o == 'D -1':
            if pq:
                heappop(pq)
        elif o.startswith('I'):
            heappush(pq, int(o[2:]))
        else:
            raise ValueError
    if not pq:
        return [0, 0]
    else:
        min_val = heappop(pq)
        _ = [-x for x in pq]
        heapify(_)
        max_val = -heappop(_)
        return [max_val, min_val]

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
#[333, -45]
#print(solution(['I 16', 'D 1'])) #[0,0]
#print(solution(['I 7', 'I 5', 'I -5' , 'D -1'])) #[7,5]
