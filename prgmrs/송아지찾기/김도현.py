
def solution(s, e):

    answer = 0
    count = 0

    # 최적화
    # s 와 e 의 관계를 보고 최적화를 해봅시다.

    visited = [False for _ in range(10001)]
    kong = [-1, 1, 5]
    location = [s]
    while location:
        print(count, location)
        for _ in range(len(location)):
            # 방문한적 있는지 없는지 체크한 뒤에 kong 을 해야합니다.
            current = location.pop(0)
            if not visited[current]:
                if current == e:
                    return count
                for k in kong:
                    if not visited[current+k] and current+k > 0:
                        visited[current] = True
                        location.append(current+k)

        count += 1

    return count


print(solution(5, 14))      # 3
print(solution(8, 3))       # -5
print(solution(1,10))       # 2
