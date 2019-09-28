

def check(skill, case):
    temp = ''
    for c in case:
        if c in skill:
            temp += c
    return True if skill.startswith(temp) else False


def solution(skill, skill_trees):
    return len([True for c in skill_trees if check(skill, c)])


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))  # 2
# X O O X