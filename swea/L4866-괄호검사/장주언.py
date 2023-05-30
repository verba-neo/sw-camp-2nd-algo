import sys

sys.stdin = open('./input.txt')

T = int(input())


def bracket(text):

    stack = []

    for char in text:
        # (이나 {가 나오면
        if char == '(' or char == '{':
            # 스택에 추가
            stack.append(char)
        # ) 혹은  }가 나왔을 때
        elif char == ')' or char == '}':
            # 스택에 아무것도 없으면 0
            if not stack:
                return 0
            # ) 일때 pop으로 마지막 값을 꺼냈는데 ( 가 아니라면 0
            elif char == ')' and stack.pop() != '(':
                return 0
            # } 일 때 pop으로 마지막 값을 꺼냈는데 {가 아니라면 0
            elif char == '}' and stack.pop() != '{':
                return 0
    # 다 꺼내고 나서 스택에 값이 남아있으면 0
    if stack:
        return 0
    else:
        return 1


for tc in range(1, T+1):
    text = list(input())
    print(f'#{tc} {bracket(text)}')
