t1 = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
r1 = 5
t2 = [['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]
r2 = 3


from collections import defaultdict
from itertools import combinations

def solution(clothes):
    answer = 1
    cloth_dict = defaultdict(list)
    
    for (item_name, item_class) in clothes:
        cloth_dict[item_class].append(item_name)
        
    groups = list(cloth_dict.values())

    for each_group in groups:
        answer *= len(each_group) + 1

    return answer-1

    '''
    if len(order_by_class) == 1:
        answer += len(list(combinations(order_by_class[0], 1)))
    else:
        for each_class in order_by_class:
            answer += len(list(combinations(each_class, 1)))
        answer += len(order_by_class)
        
    return answer
    '''

    

print(solution(t1)) #5
print(solution(t2)) #3
