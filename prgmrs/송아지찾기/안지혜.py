def solution(s, e):
    visited = [False for _ in range(10001)]
    queue = [s]
    layer = 0

    while queue:
        for _ in range(len(queue)):
            current = queue.pop(0)

            if current == e:
                return layer

            if not visited[current]:
                visited[current] = True

                for n in [-1, +1, +5]:
                    if 1 <= current + n <= 10000:
                        queue += [current + n]
        layer += 1

# 3
print(solution(5, 14))

# 5
print(solution(8, 3))

# 최적화
#     if s < e:
#         layer = (e-s) // 5
#         s += layer * 5
#     else:
#         return s - e
