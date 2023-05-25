import sys
sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):
    A, B = map(str, input().split())

    typing_cnt = 0
    including_cnt = 0
    char_idx = 0

    for idx in range(len(A)-len(B)+1):
        if A[char_idx:len(B)+char_idx] == B:
            including_cnt += 1
            char_idx = len(B) + char_idx - 1
        char_idx += 1

    typing_cnt = len(A) - len(B)*including_cnt + including_cnt

    print(f'#{tc} {typing_cnt}')





