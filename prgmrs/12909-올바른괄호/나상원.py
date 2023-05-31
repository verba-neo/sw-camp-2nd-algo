def solution(s):
    answer = True

    s_string = list(map(str, s))
    stack = []

    for char in s_string:
        if char == '(' or char == '{':
            stack.append(char)
        elif stack and char == '}' and stack[-1] == '{':
            stack.pop()
        elif stack and char == ')' and stack[-1] == '(':
            stack.pop()
        elif char == '}' or char == ')':
            stack.append(char)
    if stack:
        answer = False
    else:
        answer = True

    return answer
# True
print(solution("()()"))

# True
print(solution("(())()"))

# False
print(solution(")()("))

# False
print(solution("(()("))
