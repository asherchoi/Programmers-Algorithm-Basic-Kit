
from operator import attrgetter
from string import ascii_letters

alpabet = ascii_letters[len(ascii_letters)//2:]

class RoutingInfo():
    def __init__(self, index, distance):
        self.index = index
        self.distance = distance

    def __repr__(self):
        return "RouteInfo(index: %s, distance: %s)" %(self.index, self.distance)

def solution(name):
    name = list(name)
    handle, cur_idx = 0, 0
    
    while True:
        ### handle up down
        if name[cur_idx] != 'A': 
            handle += min_find(name[cur_idx])
            name[cur_idx] = 'A'

        ### end condition
        if name == ['A',]*len(name): 
            break

        ### route greedy
        router = []
        for i, letter in enumerate(name):
            if letter != 'A':
                rd = abs(i-cur_idx)
                ld = len(name)-rd
                router.append(RoutingInfo(i, min(rd, ld)))
        greedy = sorted(router, key=attrgetter('distance'))[0]

        ### handle right left
        handle += greedy.distance 
        cur_idx = greedy.index
            
    return handle
        

def min_find(letter):
    lidx = alpabet.find(letter)
    ridx = len(alpabet)-lidx
    return min(lidx, ridx)

print(solution("ABAABBB")) #9
print(solution("AZAAAZ")) #5
print(solution("JAZ")) #11
print(solution("JEROEN")) #56
print(solution("JAN")) #23
