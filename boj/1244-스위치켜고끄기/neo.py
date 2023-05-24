# 스위치 총 개수
N = int(input())

# 스위치 초기 상태 리스트
switches = list(map(int, input().split()))

# 학생 수
case = int(input())

for _ in range(case):
    # 성별, 스위치번호
    gender, num = map(int, input().split())
    idx = num - 1

    if gender == 1:
        i = 1
        while idx < N:
            # switches[idx] = 0 if switches[idx] else 1
            switches[idx] ^= 1  # bit operator XOR
            i += 1
            idx = (num * i) - 1
    else:
        switches[idx] ^= 1
        side = 1
        # 왼쪽은 0보다 작으면 안되고, 오른쪽은 N보다 크면 안됨
        while 0 <= (idx-side) and (idx+side) < N:
            left_idx, right_idx = idx - side, idx + side

            if switches[left_idx] != switches[right_idx]:
                break
            else:
                switches[left_idx] ^= 1
                switches[right_idx] ^= 1
                side += 1

for line_no in range(N // 20 + 2):
    start = 20 * line_no
    end = 20 * (line_no + 1)
    print(*switches[start:end])


'''
41
0 1 0 1 0 0 0 1 0 1 0 1 0 1 0 1 0 1 0 0 0 1 0 1 0 1 0 1 0 1 0 1 0 0 0 1 0 1 0 1 0
2
1 3
2 3

'''