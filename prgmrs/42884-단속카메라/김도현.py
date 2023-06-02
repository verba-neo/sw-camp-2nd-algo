def solution(routes):
    answer = len(routes)

    # for route in routes:
    #     start, end = route[0], route[1]
    #     jongbok = False
    #     for idx in range(start, end + 1):
    #         if total_routes[idx] >= 1:
    #             if not jongbok:
    #                 answer -= 1
    #             jongbok = True
    #         total_routes[idx] += 1

    answer = 0
    cam = []
    '''
    정렬을 하지 않으면
    전부 실패합니다. [[1, 5], [7, 9], [6,7]] 을 생각해보면 2개만 하면 되는데,
    정렬 안 하면 3개 설치합니다.
    각 route 마다 마지막 구간을 기준으로 CCTV 를 설치하면 가장 최적의 결과가 나올 수 있습니다.
    탐욕 GREEDY
    현재 route 가 시작이 마지막 CCTV 보다 뒤에 있으면 일단 CCTV만들면 됨. 
    '''
    routes = sorted(routes, key= lambda x:x[1])
    print(routes)
    for route in routes:
        start, end = route[0], route[1]
        joongbok = False

        # n 이 작은 cam 으로 돌아가며 확인하는 것이 시간초과 안 나옵니다.
        # idx 로 돌면 한칸한칸 다 보겠져? 효율성 테스트 3인가 4인가 시간초과입니다
        for c in cam:
            if c in range(start, end+1):
                joongbok = True
                break
        # for idx in range(start, end+1):
        #     if idx in cam:
        #         joongbok = True
        #         break
        if not joongbok:
            cam.append(end)
            answer += 1

    return answer


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3], [-3, -1]]))
print(solution([[1, 5], [7, 9], [6, 7]]))
