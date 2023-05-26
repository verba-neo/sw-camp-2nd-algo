import sys
sys.stdin = open('input.txt')

N = int(input())
switches = list(map(int, input().split()))
case = int(input())


def switching_switch(idx):
    if switches[idx]:
        switches[idx] = 0
    else:
        switches[idx] = 1


for _ in range(case):
    gender, number = map(int, input().split())

    # 남: 몇번 바꾸는지 구해서 스위치를 반대로 바꿔줌
    if gender == 1:
        times = len(switches) // number
        for i in range(times):
            switching_switch(number * (i+1) - 1)

    # 여: range를 만들고 양쪽 같으면 그만큼 range값을 변경함. 첫 스위치 번호나 끝 스위치 번호를 받으면 양쪽 비교할 필요 없으니까, 그 번호만 바꿈
    else:
        target_idx = number - 1
        num_range = [target_idx, target_idx]

        if 1 < number < N:
            while 0 not in num_range and N-1 not in num_range:
                if switches[num_range[0] - 1] == switches[num_range[1] + 1]:
                    num_range[0] -= 1
                    num_range[1] += 1
                else:
                    break

        idx_list = [i for i in range(num_range[0], num_range[1] + 1)]

        for idx in idx_list:
            switching_switch(idx)

for i in range(0, N, 20):
    print(' '.join(map(str, switches[i: i+20])))
