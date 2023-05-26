import sys
sys.stdin = open('./input.txt')
# combinations, permutations

N = int(input())

switch_status = list(map(int, input().split()))
students = int(input())


def change(num):

    if switch_status[num] == 0:
        switch_status[num] = 1
    else:
        switch_status[num] = 0
    return


for tc in range(1, students+1):
    student_mf, number = map(int, input().split())
    idx = number - 1
    if student_mf == 1:
        for switch_idx in range(1, N + 1):
            m_idx = 0
            if switch_idx % number == 0:
                m_idx = switch_idx - 1
                change(m_idx)
    else:
        change(idx)
        for mf_idx in range(N//2):
            if number + mf_idx > N or number - mf_idx < 1:
                break
            if switch_status[idx+mf_idx] == switch_status[idx-mf_idx]:
                change(idx+mf_idx)
                change(idx-mf_idx)
            else:
                break

for no in range(N//20 + 1):
    start = 20 * no
    end = 20 * (no+1)
    print(' '.join(map(str, switch_status[start:end])))
