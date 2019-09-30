

def solution(n,a,b):
    count = 0
    while a != b:
        a, b = (a+1)//2, (b+1)//2
        count += 1
    return count

