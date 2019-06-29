
from operator import itemgetter
from time import time
'''
def make_set(edges):
    _ = set([e for a in [e[:2] for e in edges] for e in a])
    global CYCLE
    CYCLE = dict(zip(_, _))

def find(node):
    if CYCLE[node] == node:
        return node
    else:
        CYCLE[node] = find(CYCLE[node]) #recursive 
        return find(CYCLE[node])

def union(n1, n2):
    CYCLE[find(n2)] = find(n1)
    
def solution(n, edges):
    edges.sort(key=itemgetter(2))
    make_set(edges)
    cost = 0
    for e in edges:
        if find(e[0]) != find(e[1]):
            union(e[0], e[1])
            cost += e[2]
    return cost
'''

### my solution time complexity
### worst case O(n^2) <-> best case O(n)

def solution(n, costs): 
    costs.sort(key=itemgetter(2))
    line = costs.pop(0)
    nodes, cost = set(line[:2]), line[2]
    while not len(nodes) == n:
        gen = ([x,y,z] for (x,y,z) in costs
                   if (x in nodes or y in nodes) \
                        and not (x in nodes and y in nodes))
        line = next(gen)
        costs.remove(line)
        nodes.update(line[:2])
        cost += line[2]
    return cost


tic = time()
print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])) #4
print(solution(4, [[0,1,1],[0,2,8],[1,2,5],[1,3,1],[2,3,8]])) #7
print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8],[0,3,1]])) #4
print(solution(4, [[0,1,1],[0,2,2],[2,3,1]])) #4
toc = time()
print(toc-tic)



'''


'''
