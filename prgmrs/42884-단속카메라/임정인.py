# greedy 탐욕법 : 가장 최적값을 계속 구해나가면 답
# 지금 선택하기에 가장 좋은 선택을 계속해나가기
# 과거에 했던 일 기록해서 푸는 문제 = DP
# 차 나가는 시간 or 들어오는 시간 선택

# 출차 기준으로 리스트 안에 딕셔너리 정렬 후, 정리
def solution(routes):

    # 필요한 카메라 수
    answer = 0
    # 출차 기준 오름차순 정렬 x[1] : 입차 관련은 정렬 안됨
    routes.sort(key = lambda x: x[1])
    key = -30001

    for route in routes:
        # 기준 카메라보다 진입 지점이 뒤에 있으면
        if route[0] > key:
            # 안 찍히므로 카메라 하나 더 필요
            answer += 1
            # 맨 끝
            key = route[1]

    return answer

# 강사님
def solution(routes):
    routes.sort(key=lambda info: info[1])

    last_camera = routes[0][1]
    answer = 1   # -15 위치에 일단 하나 설치

    for idx in range(1, len(routes)):
        start, end = routes[idx]
        if start > last_camera:
            last_camera = end
            answer += 1

    return answer

    # 람다 표현식 쓰지 않을 때
    # def x(info):
    #     return info[1]
    # routes.sort(key = x)
    # print(routes)

# 2
print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))

