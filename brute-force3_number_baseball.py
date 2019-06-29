
from itertools import permutations

def solution(baseball):
    possible = [int(str(x)+str(y)+str(z)) for (x,y,z) in list(permutations(list(range(1, 10)), 3))]
    for i, p in enumerate(possible): 
        for g,s,b in baseball:       
            if not baseball_game(p, g) == (s, b):
                possible[i] = None
    return len([x for x in possible if x != None])

def baseball_game(answer, guess):
    strike = len([(x,y) for (x,y) in zip(str(answer), str(guess)) if x==y])
    ball = len([x for x in str(guess) if x in str(answer)])
    return strike, ball-strike
    


print(baseball_game(324, 123)) #1, 1
print(baseball_game(324, 356)) #1, 0
print(baseball_game(324, 327)) #2, 0
print(baseball_game(324, 489)) #0, 1
print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))
