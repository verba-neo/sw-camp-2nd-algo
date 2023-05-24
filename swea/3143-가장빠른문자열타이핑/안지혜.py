import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()

    A_ls = list(A)
    B_first_char = B[0]
    B_len = len(B)

    count = 0
    for idx, el in enumerate(A_ls):

        # B의 첫글자로 시작하는 el을 만나면, B의 len만큼 잘라서 비교한다
        if B_first_char == el and B == ''.join(A_ls[idx:idx + B_len]):
            count += 1
            for i in range(idx, idx+B_len):
                A_ls[i] = '$'

    total = len(A_ls) - (B_len * count) + count
    answer = total

    print(f'#{tc} {answer}')
