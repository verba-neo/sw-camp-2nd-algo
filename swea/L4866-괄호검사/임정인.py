import sys
sys.stdin = open('input.txt')

# 테스트 데이터 개수
T = int(input())  # 3

for tc in range(1, T+1):

    string = input()
    stack = []
    answer = 1  # 맞다고 믿고 시작

    for char in string:
        if char == '(' or char == '{':  # if char in '({' 도 가능
            stack.append(char)  # push 쌓기

        elif char == ')':
            # last = stack.pop()  # pop 삭제

            # stack이 비어있는데 pop 하면 에러 (먼저 검증 필요)
            # stack 이 비어있지 않음을 확인한 후 pop
            if stack and '(' != stack.pop():
                answer = 0
                continue
        elif char == '}':
            # stack 이 비어있지 않음을 확인한 후 pop
            if stack and '{' != stack.pop():
                answer = 0
                break

    # 끝났는데 스택에 남은게 있다면,
    if stack:
        answer = 0

    print(f'#{tc} {answer}')


# (2) 풀이
for tc in range(1, T + 1):
    string = input()
    stack = []
    answer = 1  # 맞다고 믿고 시작

    for char in string:
        if char in '({':
            stack.append(char)

        elif char in ')}':
            if not stack:
                answer = 0
                break
            last = stack.pop()
            if (char == ')' and last != '(') or (char =='}' and last != '{'):
                answer = 0
                break

        else:
            if stack:
                answer = 0

        print(f'#{tc} {answer}')

