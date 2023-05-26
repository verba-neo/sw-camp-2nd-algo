import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    string = input()
    stack = []
    answer = 1

    for char in string:
        # 열리는 괄호면,
        if char in '({':
            stack.append(char)

        # 닫히는 괄호면,
        elif char in ')}':
            # 스택이 비어있을 때 닫히는 괄호나옴 => 에러
            if not stack:
                answer = 0
                break

            last = stack.pop()
            # 열림 닫힘 일치 확인
            if (char == ')' and last != '(') or (char == '}' and last != '{'):
                answer = 0
                break
    else:
        if stack:
            answer = 0

    print(f'#{tc} {answer}')
