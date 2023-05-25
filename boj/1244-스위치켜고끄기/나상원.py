import sys
sys.stdin = open('./input.txt')
# combinations, permutations

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
                if switch_status[m_idx] == 0:
                    switch_status[m_idx] = 1
                else:
                    switch_status[m_idx] = 0

    elif student_mf == 2:
        if switch_status[:number - 1] == switch_status[(number - 1) * 2:number - 1:-1]:
            for trans in range((number - 1) * 2 + 1):
                if switch_status[trans] == 1:
                    switch_status[trans] = 0
                elif switch_status[trans] == 0:
                    switch_status[trans] = 1
        else:
            if switch_status[number - 1] == 0:
                switch_status[number - 1] = 1
            else:
                switch_status[number - 1] = 0

for no in range(N // 20 + 1):
    start = 20 * no
    end = 20 * (no+1)
    print(' '.join(map(str, switch_status[start:end])))
