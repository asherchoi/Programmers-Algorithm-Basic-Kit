
'''
# Solve the problem within O(n) in each time/space complexities

def solution2(n, lost, reserve):
    ### initial state of students
    students = [list(x) for x in zip(range(1,n+1), [1,]*n)] 
    for student in students:
        if student[0] in lost and student[0] in reserve:
            continue
        if student[0] in lost:
            student[1] = 0 
        if student[0] in reserve:
            student[1] = 2 
    ###

    ### borrow gym suit
    for i in range(len(students)):
        if students[i][1] == 0:
            if (students[i-1][1]==2) and (i!=0): 
                students[i-1][1] -= 1
                students[i][1] += 1
            elif (i!=len(students)-1) and (students[i+1][1]==2):
                students[i+1][1] -= 1
                students[i][1] += 1
            else:
                pass
    ###

    return len([(x,y) for (x,y) in students if y != 0])
'''


def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]

    for l in _reserve:
        front, back = l-1, l+1
        if front in _lost:
            _lost.remove(front)
        elif back in _lost:
            _lost.remove(back)
            
    return n-len(_lost)



print(solution(5, [2,4], [1,3,5])) #5
print(solution(5, [2,4], [3])) #4
print(solution(3, [3,], [1,])) #2
print(solution(3, [1,2], [2,3]))
