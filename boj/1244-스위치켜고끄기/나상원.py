import sys
sys.stdin = open('./input.txt')
# combinations, permutations

def trans(number):
    if switch_status[number] == 0:
        switch_status[number] = 1
    else:
        switch_status[number] = 0
    return

N = int(input())
switch_status = list(map(int, input().split()))
students = int(input())

for tc in range(1, students+1):
    student_mf, number = map(int, input().split())
    if student_mf == 1:
        for switch_idx in range(1, N+1):
            m_idx = 0
            if switch_idx % number == 0:
                m_idx = switch_idx-1
                trans(m_idx)

    elif student_mf == 2:
        trans(number)
        for idx in range(N//2):
            if number + idx > N or number - idx < 1:
                break
            if switch_status[number + idx] == switch_status[number - idx]:
                trans(number + idx)
                trans(number - idx)
            else:
                break

for no in range(N // 20 + 1):
    start = 20 * no
    end = 20 * (no+1)
    print(' '.join(map(str, switch_status[start:end])))
