
def solution(s):
    longest = 0
    for i in range(0, len(s)):
        for j in range(i+1, len(s)+1):
            if is_palindrome(s[i:j]) and j - i > longest:
                longest = j - i
    return longest


def is_palindrome(s):
    mid = (len(s)+1)//2
    return True if s[:mid] == s[len(s)-mid:][::-1] else False

print('>Problem 0')
print(solution("baaab"))  # 13
print('>Problem 1')
print(solution("abcdcba"))  # 7
print('>Problem 2')
print(solution("abacde"))  # 3
print('>Problem 3')
print(solution("cdeaba"))  # 3
print('>Problem 4')
print(solution("c"))  # 1
