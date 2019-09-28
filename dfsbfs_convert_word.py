
from collections import deque, defaultdict


def similar(word1, word2):
    cnt = 0
    for w1, w2 in zip(word1, word2):
        if w1 != w2:
            cnt += 1
    return True if cnt == 1 else False


def to_adj_list(words):
    adj = defaultdict(set)
    for w in words:
        for _w in words:
            if w != _w and similar(w, _w):
                adj[w].update({_w})
    return adj


def solution(begin, target, words):
    adj = to_adj_list([begin] + words)
    print(adj)
    ans = 0
    queue = deque([(begin, [begin])])  # start node, path

    while queue:
        n, path = queue.popleft()
        if n == target:
            ans = len(path)-1
            break
        else:
            for m in adj[n]-set(path):
                queue.append((m, path+[m]))

    return ans


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0
