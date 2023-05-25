import sys
sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):
    A, B = map(str, input().split())

    result_cnt = 0
    in_cnt = 0
    char_idx = 0

    for c_idx in range(len(A)-len(B)+1):
        if A[char_idx:len(B)+char_idx] == B:
            in_cnt += 1
            char_idx = len(B)+char_idx - 1
        char_idx += 1
    result_cnt = len(A) - len(B)*in_cnt + in_cnt

    print(f'#{tc} {result_cnt}')
