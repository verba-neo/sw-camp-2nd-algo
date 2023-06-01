def solution(routes):

    routes.sort(key=lambda x: x[1])

    # print(routes)

    answer = 0

    for idx_cu in range(len(routes)):
        std_car, dep_car = routes[idx_cu]
        for idx_nxt in range(1, len(routes)):
            nxt_std_car, nxt_dep_car = routes[idx_nxt]
            if nxt_std_car > dep_car:
                dep_car = nxt_dep_car
                answer += 1

    # last_camera = routes[0][1]
    # answer = 1
    #
    # for idx in range(1, len(routes)):
    #     start, end = routes[idx]
    #     if start > last_camera:
    #         last_camera = end
    #         answer += 1
    #
    return answer


routes = [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]
print(solution(routes))
