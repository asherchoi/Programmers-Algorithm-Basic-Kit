t1 = ['119', '97674223', '1195524421']
r1 = False
t2 = ['123','456','789']
r2 = True
t3 = ['12','123','1235','567','88']
r3 = False

'''
def solution(phone_book):
    answer = True
    phone_book.sort()
    for index in range(len(phone_book)-1):
        if phone_book[index+1].startswith(phone_book[index]):
            answer = False 
    return answer
'''

def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book, key=len)
    
    return answer
    
print(solution(t1)==r1)
print(solution(t2)==r2)
print(solution(t3)==r3)
