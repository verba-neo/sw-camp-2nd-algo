import sys
sys.stdin = open('./input.txt')

# T = int(input())
T = 10

for tc in range(1, T+1):
    size = int(input())
    table = [list(map(int, input().split())) for _ in range(size)]

    count = 0
    for col in range(size):  # 열 탐색
        stack = []
        row = 0
        while row < size:
            if not stack and table[row][col] == 1:  # 스택이 비어있고, 값이 1이면 넣고
                stack.append(1)
            elif stack and table[row][col] == 2:  # 스택이 남아 있고, 값이 2이면 pop 하고 값 더하기
                count += stack.pop()
            row += 1 ## row 인덱스 증가

    print(f'#{tc} {count}')
