import sys
sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):
    M = input()

    now_stick = 0
    cut_stick = 0

    for cut_idx in range(len(M)):
        if M[cut_idx] == '(':
            now_stick += 1
        else:
            if M[cut_idx-1] == '(':
                now_stick -= 1
                cut_stick += now_stick
            else:
                now_stick -= 1
                cut_stick += 1

    print(f'#{tc} {cut_stick}')