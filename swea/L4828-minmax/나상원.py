import sys
sys.stdin = open('./input.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))

    answer = 0
    max_num = 0
    min_num = number[0]

    for mx_num in number:
        if max_num <= mx_num:
            max_num = mx_num

    for mi_num in number:
        if min_num >= mi_num:
            min_num = mi_num

    answer = max_num - min_num


    print(f'#{tc} {answer}')

