
def solution(people, limit):
    people.sort()
    length=len(people)
    light, heavy, boat = 0, length-1, 0
    
    while light < heavy:
        if people[light]+people[heavy] <= limit:
            boat+=1
            light+=1
        heavy -= 1
        
    return length-boat

print(solution([70, 50, 80, 50], 100)) #3
print(solution([70, 80, 50], 100)) #3
print(solution([40, 40, 40], 100)) #2
print(solution([10,20,30,40,50,60,70,80,90], 100)) #5
