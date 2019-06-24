
def solution(brown, red):
    for j in range(1, int(red**(1/2))+1):
        if red%j == 0:
            i = int(red/j)
            if (i+2)*(j+2)-red == brown:
                return [i+2,j+2]
        

print(solution(10, 2)) #[4,3]
print(solution(8, 1)) #[3, 3]
print(solution(24, 24)) #[8, 6]
