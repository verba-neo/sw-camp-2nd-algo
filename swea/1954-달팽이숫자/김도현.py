import sys
sys.stdin = open('input.txt')

T = int(input())

move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for t in range(1, T+1):

    N = int(input())
    answer = [[0]*N for _ in range(N)]
    number = 1
    x, y = 0, 0
    answer[0][0] = 1
    while number < N*N:
        for m in move:
            my, mx = m[0], m[1]
            while number < N*N:
                if y+my <= N-1 and y+my >= 0 and x+mx <= N-1 and x+mx >= 0:
                    if answer[y+my][x+mx] == 0:
                        number += 1
                        answer[y+my][x+mx] = number
                        x += mx
                        y += my
                    else:
                        break
                else:
                    break

    print(f'#{t}')
    for a in answer:
        for i in a:
            print(i, end=' ')
        print()
