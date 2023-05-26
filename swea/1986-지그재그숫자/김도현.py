# start.txt.txt  파일을 한줄씩 (stdin) 입력 (open)
import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    numbers = int(input())

    answer = 0
    for n in range(numbers+1):
        if n % 2:
            answer += n
        else:
            answer -= n

    print(f'#{tc} {answer}')
