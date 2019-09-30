
def to_adj(edges):
    from collections import defaultdict
    adj = defaultdict(set)
    for sp, ep in edges:
        adj[sp].add(ep)
    return adj


def solution(n, edges):
    from collections import deque
    edges = sorted([sorted(e) for e in edges])
    adj = to_adj(edges)
    #print(edges)
    print(adj)
    visit = []
    queue = deque([1])
    level = 0
    while queue:
        n = queue.popleft()
        except_level = [v[1] for v in visit]
        if n not in except_level:
            visit.append((level, n))
            queue += adj[n] - set(except_level)
    print(visit)




solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])  # 3
solution(7, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2], [5, 7]])  # 1