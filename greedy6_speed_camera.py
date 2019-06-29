
from operator import itemgetter

def solution(routes):
    routes.sort(key=itemgetter(1), reverse=True)
    camera = 0
    while routes:
        r = routes.pop()
        camera += 1
        while True:
            if routes and routes[-1][0] <= r[1] and routes[-1][1] >= r[1]:
                routes.pop()
            else:
                break
    return camera
    

print(solution([[0, 0], [-1, 0], [0, 0], [2, 3], [0, 0]])) #2
print(solution([[-2, -1], [1, 2],[-3, 0]])) #2
print(solution([[0, 1], [0, 1], [1, 2]])) #1
print(solution([[0, 1], [2, 3], [4, 5], [6, 7]])) #4
print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]])) #2
print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]])) #2
print(solution([[-20, 15], [-20, -15], [-14, -5], [-18, -13], [-5, -3]])) #2
