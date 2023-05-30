def solution(ability):
    answer = 0
    # 학생 수
    student_count = len(ability)
    # 종목 수
    sport_count = len(ability[0])
    # 스쿼드 학생 포함 여부
    visited = [False for _ in range(student_count)]

    def dfs(sport_idx, total):
        # sport_idx => 어떤 종목을 확인하는 중인지
        # total => 현재까지의 반 능력치 총합
        nonlocal answer
        # 스쿼드 완성
        if sport_idx == sport_count:
            # 현재의 총합이 최대라면,
            if total > answer:
                answer = total
            return

        # 학생들을 한명씩 스쿼드에 추가
        for student_idx in range(student_count):
            # 스쿼드에 없는 학생일 경우
            if not visited[student_idx]:
                # 포함 시키고
                visited[student_idx] = True
                # 스쿼드에 다른 학생 추가하러 이동, 현재 포함시킨 학생의 능력치를 total에 추가
                dfs(sport_idx + 1, total + ability[student_idx][sport_idx])
                # 확인 했다면, 해당 학생은 스쿼드에서 뺌
                visited[student_idx] = False

    dfs(0, 0)

    return answer


# 210
print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))

# 60
print(solution([[20, 30], [30, 20], [20, 30]]))