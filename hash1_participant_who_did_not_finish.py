
p1 = ['leo', 'kiki', 'eden']
c1 = ['eden', 'kiki']
r1 = 'leo'

p2 = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
c2 = ['josipa', 'filipa', 'marina', 'nikola']
r2 = 'vinko'

p3 = ['mislav', 'stanko', 'mislav', 'ana']
c3 = ['stanko', 'ana', 'mislav']
r3 = 'mislav'



def solution(participant, completion):

    participant.sort()
    completion.sort()

    answer = ''
    
    for index in range(len(completion)):
        if participant[index]!=completion[index]:
            answer = participant[index]
            break
    else:
        answer = participant[-1]
        
    return answer

print(solution(p1, c1)==r1)
print(solution(p2, c2)==r2)
print(solution(p3, c3)==r3)

    



