def solution(s):

    stack = []

    for char in s:

        if char == '(':
            stack.append(char)

        elif char == ')':
            if not stack:
                return False
            elif char == ')' and stack.pop() != '(':
                return False

    if stack:
        return False
    else:
        return True



# True
print(solution("()()"))

# True
print(solution("(())()"))

# False
print(solution(")()("))

# False
print(solution("(()("))