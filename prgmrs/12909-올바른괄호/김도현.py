def solution(s):
    # ?
    answer = True

    if s[0] == ")" or s[-1] == "(":
        answer = False
    elif s.count("(") != s.count(")"):
        answer = False

    tmp = 0
    for i in range(len(s)):
        if s[i] == ")":
            tmp -= 1
        else:
            tmp += 1

        if tmp < 0:
            return False

    return answer

    # # stack 으로 풀어보기
    # answer = True
    #
    # stack = [s[0]]
    #
    # if s[0] == ")" or s[-1] == "(":
    #     answer = False
    # elif s.count("(") != s.count(")"):
    #     answer = False
    # 
    # for g in s[1:]:
    #     tmp = ''
    #     if stack:
    #         tmp = stack.pop()
    #
    #     if tmp == '(' and g == '(':
    #         stack.append(g)
    #     elif tmp == '(' and g == ')':
    #         continue
    #     elif tmp == ')':
    #         return False
    #
    # if stack:
    #     return False
    #
    # return answer
    # # 왜틀려왜
