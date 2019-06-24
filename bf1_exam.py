
def solution(test):
    l = len(test)
    patterns = [[1,2,3,4,5]*(l//5+1),
                [2,1,2,3,2,4,2,5]*(l//7+1),
                [3,3,1,1,2,2,4,4,5,5]*(l//9+1)
                ]
    
    correct_count = {}
    for i, pattern in enumerate(patterns):
        submit = pattern[:len(test)]
        correct_count[i+1] = (len([(x,y) for x,y in zip(test, submit) if x==y]))

    leading = max(correct_count.values())
    return [x for (x,y) in correct_count.items() if y==leading]


print(solution([1,2,3,4,5])) # [1, ]
print(solution([1,3,2,4,2])) # [1,2, 3]
