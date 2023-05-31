def solution(ability):
    answer = 0

    students = len(ability)
    items = len(ability[0])
    attend_st = [False for _ in range(students)]

    def dfs(items_idx, total):
        nonlocal answer

        if items_idx == items:
            if total > answer:
                answer = total
            return

        for students_idx in range(students):
            if not attend_st[students_idx]:
                attend_st[students_idx] = True

                dfs(items_idx+1, total + ability[students_idx][items_idx])

                attend_st[students_idx] = False
    dfs(0, 0)
    return answer


ability = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]
print(solution(ability))
