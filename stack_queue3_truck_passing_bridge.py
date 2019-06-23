
from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_len = len(truck_weights)
    wait, inbridge, outbridge = deque(truck_weights), deque(), deque()  
    timer, cur_bridge_weight = 1, 0

    while not len(outbridge) == truck_len:
        if wait:
            enter_truck = wait.popleft()
            
            #if bridge available(current bridge weight + willing to enter truck)
            if weight >= cur_bridge_weight + enter_truck:
                #access
                inbridge.append([enter_truck, 0]) #enter truck weight & start timer
                cur_bridge_weight += enter_truck # current bridge weight is increased
            else:
                # retore at wait
                wait.appendleft(enter_truck)

        for truck in list(inbridge):
            truck[1] += 1
            if truck[1] == bridge_length: # if time to get out
                getout_truck = inbridge.popleft()
                cur_bridge_weight -= getout_truck[0]
                outbridge.append(getout_truck)
                
        timer += 1

    return timer

print(solution(2, 10, [7,4,5,6])) #8
print(solution(100, 100, [10])) #101
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10])) #110
