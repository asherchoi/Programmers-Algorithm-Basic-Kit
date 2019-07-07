
def solution(budgets, M):
    left, right = 0, max(budgets)
    
    while right >= left:
        mid = (left+right) // 2
        amount = sum([b if mid > b else mid for b in budgets])
        if amount > M:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
            
    return answer
    
        
       
print(solution([110, 120, 140, 150], 485)) #127
print(solution([110, 120, 140, 150], 400)) #100
print(solution([110, 120, 100, 100], 450)) #120
