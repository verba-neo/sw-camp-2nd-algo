import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N_M = input().split()
    N = int(N_M[0])
    M = int(N_M[1])

    a_ls = list(map(int, input().split()))

    sum_list = []
    for i in range(N-M+1):
        cur_sum = 0
        for extra_i in range(M):
            cur_sum += a_ls[i+extra_i]

        sum_list.append(cur_sum)

    max_sum = max(sum_list)
    min_sum = min(sum_list)

    answer = max_sum - min_sum

    print(f'#{tc} {answer}')
