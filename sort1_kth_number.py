
from heapq import nsmallest

def solution(array, commands):
    return [nsmallest(k, array[s-1:e])[-1] for s, e, k in commands]
    

print(solution([1,5,2,6,3,7,4], [[2,5,3], [4,4,1], [1,7,3]])) #[5, 6, 3]
