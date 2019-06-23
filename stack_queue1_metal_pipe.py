arrangement = '()(((()())(())()))(())'

def solution(arrangement):
    queue = list(arrangement)
    answer, level = 0, 0
    
    cur_token = queue.pop(0)
    while queue:
        look_a_head = queue.pop(0)
        
        if cur_token == '(':
            if look_a_head == ')':
                answer += level
            elif look_a_head == '(':
                level += 1
            else:
                raise SyntaxError('invaild arrangement')
            
        elif cur_token == ')':
            if look_a_head == ')':
                level -= 1
                answer += 1
            elif look_a_head == '(':
                pass
            else:
                raise SyntaxError('invaild arrangement')
        
        else:
            raise SyntaxError('invaild arrangement')

        cur_token = look_a_head

    return answer

print(solution(arrangement)) #17
