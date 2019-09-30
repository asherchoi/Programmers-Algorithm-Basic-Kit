
def solution(s):
    return ' '.join([w[0].upper() + w[1:].lower() for w in s.split()])

print(solution("m")) #	M
print(solution("3people unFollowed me")) #	3people Unfollowed Me
print(solution("for the last week")) #	For The Last Week