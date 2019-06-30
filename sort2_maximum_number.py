
from functools import cmp_to_key

def comparator(x, y):
    xy, yx = x+y, y+x
    # xy > yx return 1 / xy < xy return -1 / xy == yz return 0
    return (int(xy)>int(yx))-(int(xy)<int(yx)) 

def solution(numbers):
    n = list(map(str, numbers))
    n.sort(key=cmp_to_key(comparator), reverse=True)
    return str(int(''.join(n)))


'''
def solution(numbers): #[3, 34, 30, 5, 9]
    numbers = list(map(str, numbers)) #['3', '34', '30', '5', '9']
    numbers.sort(key=lambda x: x*3, reverse=True) # ['303030', '333', '343434', '555', '999']
    return str(int(''.join(numbers)))

# String comparator 
# '303030' < '333' == True
'''


'''
def left_is_bigger(x, y):
    x, y = str(x), str(y)
    iteration = max(len(x), len(y))
    answer = False
    for _ in range(iteration+1):
        x_first, x_rest = x[0], x[1:]
        y_first, y_rest = y[0], y[1:]
        if x_first > y_first:
            answer = True
            break
        elif x_first < y_first:
            break
        else:
            x = x_rest + x_first
            y = y_rest + y_first
    return answer

def right_is_bigger(x, y):
    x, y = str(x), str(y)
    iteration = max(len(x), len(y))
    answer = False
    for _ in range(iteration+1):
        x_first, x_rest = x[0], x[1:]
        y_first, y_rest = y[0], y[1:]
        if x_first < y_first:
            answer = True
            break
        elif x_first > y_first:
            break
        else:
            x = x_rest + x_first
            y = y_rest + y_first
    return answer


def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[len(numbers)//2]
    left, right, equal =[], [], []
    for n in numbers:
        if left_is_bigger(n, pivot):
            left.append(n)
        elif right_is_bigger(n, pivot):
            right.append(n)
        else:
            equal.append(n)
    return quicksort(left) + equal + quicksort(right)

def solution(numbers):
    return str(int(''.join([str(x) for x in quicksort(numbers)])))
        
'''
print(solution([3, 34, 30, 5, 9])) #9534330
print(solution([6, 10, 2])) #6210



assert "40403" == solution([40, 403]) #40 win
assert "40540" == solution([40, 405]) #405 win
assert "40440" == solution([40, 404]) #404 win
assert "12121" == solution([12, 121]) #12 win
assert "21221" == solution([21, 212]) #212 win
assert "223222" == solution([2, 22, 223])
assert "41541" == solution([41, 415])
assert "9534330" == solution([34, 3, 30, 5, 9])
assert "981000" == solution([1000, 9, 8])
assert "1000000" == solution([1000, 0, 0, 0])
assert "70000" == solution([70, 0, 0, 0])
assert "0" == solution([0, 0, 0, 0])
assert "222" == solution([2, 22])
assert "1" == solution([1])

