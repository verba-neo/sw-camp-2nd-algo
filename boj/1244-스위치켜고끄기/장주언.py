# 1부터 연속적으로 번호가 붙어있는 스위치가 있다.
# 스위치는 켜져있거나 꺼져있다.
# 1은 켜져있음을 0은 꺼져있음을 나타낸다.
# 학생들에게 자연수를 나누어준다.
# 남학생은 스위치 번호가 자기가 받은 수의 배수이면 그 스위치의 상태를 바꾼다
# 여학생은 자기가 받은 수의 번호가 붙은 스위치를 중심으로 좌우대칭 바꾼다.


# 함수설정

def change(i):

    if switches[i] == 1:
        switches[i] = 0
    else:
        switches[i] = 1
    return

# 스위치 개수
N = int(input())
# 스위치 상태
switches = list(map(int, input().split()))

student = int(input())

for n in range(1, student+1):
    gender, number = list(map(int,input().split()))

    if gender == 1:
        for i in range(number-1, len(switches), number):
            change(i)

    else:
        change(number-1)
        for k in range(1, len(switches)//2):
            if (number + k) > len(switches) or (number - k) <1 :
                break
            if switches[number-1+k] == switches[number-1-k]:
                change(number-1+k)
                change(number-1-k)
            else:
                break

for i in range(0, N, 20):
    print(' '.join(map(str, switches[i: i+20])))

