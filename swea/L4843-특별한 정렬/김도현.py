import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):

    N = int(input())
    numbers = list(map(int, input().split()))
    answer = []

    numbers.sort()
    for i in range(N):
        # print(numbers[-i-1])
        if len(answer) == 10:
            break
        answer.append(numbers[-i-1])
        answer.append(numbers[i])

    # 출력을 위한 변환
    answer_out = ' '.join(map(str,answer))
    print(f'#{t} {answer_out}')
