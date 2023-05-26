import sys
sys.stdin = open('./input.txt')

T = int(input())


def find(string):
    stack = []
    for char in text:
        # 열리는 괄호라면,
        if char == '(' or char == '{':
            stack.append(char)
        # 비어 있지 않고 닫는 괄호가 있고 전 스택에 연 괄호가 있다면,
        elif stack and char == '}' and stack[-1] == '{':
            stack.pop()
        elif stack and char == ')' and stack[-1] == '(':
            stack.pop()
        elif char == '}' or char == ')':
            stack.append(char)

    # stack 에 남은게 있다면,
    if stack:
        return 0
    else:
        return 1


for tc in range(1, T+1):
    text = input()

    print(f'#{tc} {find(text)}')
