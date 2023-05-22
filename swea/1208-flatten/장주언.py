# 가장 높은 곳에 있는 상자를 가장 낮은 곳으로 이동 시키는 것을 덤프라고 한다.
# 덤프 횟수를 제한 하였을 때 최고점과 최저점의 차이를 구하라

import sys

sys.stdin = open('./input.txt')

T = 10

for tc in range(1, T + 1):
    # 덤프 횟수
    dump = int(input())
    # 상자의 높이
    box_height = list(map(int, input().split()))



   # 덤프 횟수만큼 최고점에서 최저점을 이동시키자.
    for num in range(dump):
       max_height = max(box_height)
       min_height = min(box_height)

       max_idx = box_height.index(max_height)
       min_idx = box_height.index(min_height)

       box_height[max_idx] -= 1
       box_height[min_idx] += 1

       if box_height[max_idx] - 1 == box_height[min_idx]:

            break

    answer = max(box_height) - min(box_height)

    print(f'#{tc} {answer}')





