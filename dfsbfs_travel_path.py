
def dfs(tickets, start):
    usable = [e for e in tickets if e[0] == start[-1]]
    if not usable:
        if tickets:
            return False
        else:
            return start

    for ticket in usable:
        result = dfs(tickets[:tickets.index(ticket)] + tickets[tickets.index(ticket)+1:], start + [ticket[1]])
        if result:
            return result

    return False


def solution(tickets):
    tickets.sort()
    return dfs(tickets,["ICN"])


print('Problem 1')
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["SFO", "ATL"],
                ["ATL", "ICN"], ["ATL", "SFO"], ["ATL", "SFO"]]))
# ['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO', 'ATL', 'SFO']

print('Problem 2')
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# [ICN, JFK, HND, IAD]


