import sys
sys.stdin = open('input.txt')

T = int(input())


for t in range(1, T+1):
    string = input()
    answer = 0

    gwalho = ''

    for s in string:
        if s in "{}()[]":
            gwalho += s

    while gwalho:
        if not gwalho:
            break
        elif '{}' in gwalho:
            gwalho = gwalho.replace('{}', '')
            answer = 1
        elif '()' in gwalho:
            gwalho = gwalho.replace('()', '')
            answer = 1
        elif '[]' in gwalho:
            gwalho = gwalho.replace('[]', '')
            answer = 1
        # 그냥 else 라고 해도 될듯
        elif gwalho:
            answer = 0
            break

    print(f'#{t} {answer}')

    # 스택으로 어케 푸나염
    # stack 으로 사용하기 위해서
    stack = []
    answer = 1
    for char in string:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            # stack 이 없다면 pop 을 못 합니다. error 가 발생하니 stack 의 유무를 먼저 확인해야 합니다.
            if stack and '(' != stack.pop():
                answer = 0
                break
        elif char == '}':
            if stack and '{' != stack.pop():
                answer = 0
                break
    # stack 에 남은 게 있다면
    if stack:
        answer = 0
