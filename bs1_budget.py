
def solution(budgets, M):
    left, right = 0, max(budgets)
    temp = 0
    
    while right >= left:
        mid = (left+right) // 2
        result=0
        for b in budgets:
            if mid > b:
                result += b
            else:
                result += mid  
        if result > M:
            right = mid - 1
        else:
            if result >= temp:
                answer = mid
            left = mid + 1
            
    return answer
    
        
       
print(solution([110, 120, 140, 150], 485)) #127
print(solution([110, 120, 140, 150], 400)) #100
print(solution([110, 120, 100, 100], 450))
