import sys
sys.stdin = open('./input.txt')

# T = int(input())
T = 10
for tc in range(1, T + 1):
    # 세대 개수
    N = int(input())
    H = list(map(int, input().split()))

    house_count = 0

    for idx in range(2, N - 2):
        left_apt_2 = H[idx] - H[idx - 2]
        left_apt_1 = H[idx] - H[idx - 1]
        right_apt1 = H[idx] - H[idx + 1]
        right_apt2 = H[idx] - H[idx + 2]

        if left_apt_2 > 0 and left_apt_1 > 0 and right_apt1 > 0 and right_apt2 > 0:
            house_count += min(left_apt_2, left_apt_1, right_apt1, right_apt2)

    print(f'#{tc} {house_count}')
