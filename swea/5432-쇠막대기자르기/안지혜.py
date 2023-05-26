import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = input()

    L_with_sticks = [*N.replace('()', 'L')]
    # ['L', '(', '(', '(', 'L', 'L', ')', '(', 'L', ')', 'L', ')', ')', '(', 'L', ')']

    # '(' 만나면 스틱 1개 생성
    # 'L' 만나면 스틱 갯수대로 총합에 더하기
    # ')' 만나면 스틱에서 1개 차감, 총합에 1더하기
    stage = 0
    total = 0
    for idx, el in enumerate(L_with_sticks):
        if el == '(':
            stage += 1
        elif el == 'L':
            total += stage
        elif el == ')':
            stage -= 1
            total += 1

    answer = total

    print(f'#{tc} {answer}')
