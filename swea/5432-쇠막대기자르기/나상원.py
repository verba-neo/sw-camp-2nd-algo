import sys
sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T+1):
    N = input()

    # 현재의 막대 수
    now_stick = 0
    # 잘린 막대 수
    cut_stick = 0

    # 길이 만큼 반복
    for l_stick in range(len(N)):
        # '(' 시작하면 일단 현재의 막대에 더함
        if N[l_stick] == '(':
            now_stick += 1
        # ')' 니까 레이저로 판단
        else:
            now_stick -= 1
            # 현재가 ')'
            if N[l_stick-1] == '(':
                cut_stick += now_stick
            else:
                cut_stick += 1

    print(f'#{tc} {cut_stick}')
