# from sys import stdin

n = int(input())
switch = [-1]+list(map(int, input().split()))
students = int(input())

# 스위치 켜고 끄는 함수
def change(num):
    if switch[num]:
        switch[num] = 0
    else:
        switch[num] = 1
    return

for _ in range(students):
    gender, num = map(int, input().split())  # 1 3 / 2 3
    if gender == 1:  # 남자면
        for i in range(num, n+1, num):  # 배수 찾기
            change(i)  # 해당 되는 배수만 change
    else:  # 여자면
        change(num)  # 자기 자신부터 변경 > 좌우가 어떻든 자신은 바뀌기 때문에
        for j in range(n//2):  # 범위 반으로 나눠서 탐색
            if num+j > n or num-j < 1:  # 범위 넘어가면 break, num+j > 8 or num-j < 1
                break
            if switch[num+j] == switch[num-j]:  # 좌우 같을 때
                change(num+j)  # 변경
                change(num-j)

            else:  # 좌우 다를 때
                break

for i in range(1, n+1):  # 20씩 끊어서 print 해주기
    print(switch[i], end = '')
    # if i%20 == 0:
    #     print()

# 출처 https://blue-coding-story.tistory.com/125


# (2)
# 스위치 총 개수
N = int(input())

# 스위치 초기 상태 리스트
switches = list(map(int, input().split()))

# 학생 수
case = int(input())

for _ in range(case):
    gender, num = map(int, input().split())
    idx = num - 1  # idx화 시켜주기

    if gender == 1:  # 남학생
        i = 1
        while idx < N:  # N = 스위치 총 개수
            # switches[idx] = 0 if switches[idx] else 1
            # if switches[idx]:
            #     switches[idx] = 0
            # else:
            #     switches[idx] = 1  이것도 가능

            # 이진 비트 연산 (이진법=비트)
            # 3 & 4 = 0 / 2 & 3 = 2 / 1 & 2 = 0
            # and(&) :  각 자리 수가 하나라도 0이면 0
            # or(|) : 각 자리 수가 하나라도 1이면 1
            # XOR(^) : 자리 수가 같으면 0, 다르면 1

            switches[idx] ^= 1  # bit operator XOR
            i += 1  # 배수로 만들려고
            idx = (num * i) - 1
    else:
        switches[idx] ^= 1
        side = 1
        # 왼쪽은 0보다 작으면 안되고, 오른쪽은 N보다 크면 안됨
        while 0<= (idx-side) and (idx+side) < N:
            left_idx = idx-side
            right_idx = idx+side

            if switches[left_idx] != switches[right_idx]
                break
            else:
                switches[left_idx] ^= 1
                switches[right_idx] ^= 1
                side += 1

for line_no in range(N // 20 + 1):
    start = 20 * line_no
    end = 20 * (line_no + 1)
    # print(*switches[start:end])
    print(' '.join(map(str, switches[start:end])))

    # for i in range(0, N, 20):
    #     print(' '.join(map(str, switches[i: i + 20])))

# from itertools import combinations # 조합 (순서 상관 X)
# list(combinations(range(1, 13), 3))
# # 다 더해 보고 220개 중 원하는 값 출력
#
# from itertools import permutations # 순열 (순서 상관, 모든 경우 다 출력)
# list(permutations(range(1, 13), 3))