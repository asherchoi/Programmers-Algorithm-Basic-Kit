
from collections import deque
from math import ceil

def solution(progresses, speeds):
    answer = []
    progresses_len = len(progresses)
    time_to_complete = [None]*progresses_len
    
    for i in range(progresses_len):
        time_to_complete[i] = ceil((100-progresses[i]) / speeds[i])

    while time_to_complete:
        for i in range(len(time_to_complete)):
            time_to_complete[i] -= 1

        print(time_to_complete)
        if not time_to_complete[0]:
            temp = []
            for t in time_to_complete[:]:
                if t <= 0:
                    temp.append(time_to_complete.pop(0))
                else:
                    break
            answer.append(len(temp))
        
    return answer


print(solution([93, 30, 55], [1, 30, 5])) # [2, 1]
