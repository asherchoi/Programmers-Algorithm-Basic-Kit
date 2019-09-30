
def solution(s):
    if s[0] != "(":
        return False
    stack = []
    for letter in s:
        if letter == "(":
            stack.append(letter)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return False if stack else True


print(solution("()()"))  #	true
print(solution("(())()"))  # true
print(solution(")()("))  # false
print(solution("(()("))  # false