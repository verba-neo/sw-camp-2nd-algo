# 현수의 위치 s, 송아지의 위치 e
def solution(s, e):
    # 현수의 위치가 송아지의 위치보다 값이 작은 경우
    if s < e:
        count = (e-s) // 5
        s = s + (count * 5)
    # 현수의 위치가 송아지의 위치보다 값이 큰 경우
    else:
        return s - e

    to_visit = [s]

    visited = [False for _ in range(10001)]

    while to_visit:

        for _ in range(len(to_visit)):
            current = to_visit.pop(0)

            for next_ in [current+1, current-1, current+5]:
                if next_ == e:

                    return count
                elif 0 < next_ <= 10000 and not visited[next_]:
                    visited[current] = True
                    to_visit.append(next_)
            count += 1


# 3
print(solution(5, 14))

# 5
print(solution(8, 3))

# def solution(s, e):
#
#     count = 0
#
#     to_visits = [s]
#
#     visited = [False for _ in range(10001)]
#
#     while to_visits:
#         for _ in range(len(to_visits)):
#
#             current = to_visits.pop(0)
#
#             if not visited[current]:
#
#                 visited[current] = True
#
#                 if current == e:
#                     return count
#                 for nxt in [current+1, current -1, current+5]:
#                     if 0 < nxt <= 10000 and not visited[nxt]:
#                         to_visits.append(nxt)
#     count += 1

