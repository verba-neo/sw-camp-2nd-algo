def solution(routes):
    # 끝지점 순서대로 정렬
    # 첫 route 끝지점에 겹치는 것들 제외하고 바로 그 다음것 끝지점으로 다시 지정, cam + 1
    sorted_routes = routes[:]
    sorted_routes.sort(key=lambda r: r[1])
    print(sorted_routes)
    target_end = sorted_routes[0][1]
    cam = 1

    for i in range(1, len(sorted_routes)):
        if sorted_routes[i][0] > target_end:
            target_end = sorted_routes[i][1]
            cam += 1

    return cam


# 2
print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
