import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    dump = int(input())
    box_list = list(map(int, input().split()))

    # 단순히 max min
    highest = max(box_list)
    lowest = min(box_list)

    while dump:
        highest = max(box_list)
        lowest = min(box_list)

        if highest - lowest < 2:
            break

        box_list[box_list.index(highest)] -= 1
        box_list[box_list.index(lowest)] += 1
        dump -= 1

    # 다시 체크 안 하면 #6 에서 에러남.
    highest = max(box_list)
    lowest = min(box_list)

    print(f'#{t} {highest - lowest}')

    # sort 로 사용해서 푸는 방법도 있음.
    # sort 가 시간복잡도가 더 많은 시간을 소요함.
