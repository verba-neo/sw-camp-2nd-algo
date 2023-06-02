def dfs(numbers_list, target, idx, value):
    global answer

    N = len(numbers_list)

    if idx == N:
        if value == target:
            answer += 1
        return

    dfs(numbers_list, target, idx+1, value + numbers_list[idx])
    dfs(numbers_list, target, idx+1, value - numbers_list[idx])


def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers, target, 0, 0)

    return answer


# 5
print(solution([1, 1, 1, 1, 1], 3))

# 2
print(solution([4, 1, 2, 1], 4))
