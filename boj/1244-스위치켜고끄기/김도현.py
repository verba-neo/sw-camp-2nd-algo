N = int(input())

sw = list(map(int, input().split()))
sw_dict = {k+1: v for k, v in enumerate(sw)}

students = int(input())


def change(v):
    if v == 0:
        return 1
    else:
        return 0


for s in range(students):
    gender, number = map(int, input().split())
    # print(sw_dict)

    if gender == 1:
        for k, v in sw_dict.items():
            if k % number == 0:
                sw_dict[k] = change(v)
    else:
        i = 1
        # 삼항연산자가 있습니다.
        # sw_dict[number] = 0 if sw_dict[number] else 1
        # 비트연산자?
        # sw_dict[number] ^= 1
        # 비트연산자 중 XOR(^)를 써서 X ^ 1 을 하면 X가 1이든 0이든 간에 반대로 바뀜.
        sw_dict[number] = change(sw_dict[number])
        while number + i <= len(sw) and number - i > 0:
            if sw_dict[number+i] == sw_dict[number-i]:
                sw_dict[number+i] = change(sw_dict[number+i])
                sw_dict[number-i] = change(sw_dict[number-i])
            else:
                break
            i += 1
            # i 를 증가시키는 게 if true 일 때로 옮기는 게 보기 좋지 않을까 생각.
            # sw_dict[number] 를 생각 못했을 때, 적은 거임.


answer = ' '.join(map(str, list(sw_dict.values())))
for i in range(0, len(answer), 40):
    print(answer[i:i+40])

    # print(sw_dict)
