def solution(ability):
    visited = [False for _ in range(len(ability))]
    answer = 0

    def dfs(sport_i, total):
        nonlocal answer

        if sport_i == len(ability[0]):
            answer = total if total > answer else answer
            return


        for student_i in range(len(ability)):
            if not visited[student_i]:
                visited[student_i] = True
                dfs(sport_i + 1, total + ability[student_i][sport_i])
                visited[student_i] = False

    dfs(0, 0)
    return answer


# 210
print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))

# 60
print(solution([[20, 30], [30, 20], [20, 30]]))