<<<<<<< HEAD
def dfs(numbers, target, idx, values):
    global answer

    if idx == len(numbers) and values == target:
        answer += 1
        return
    elif idx == len(numbers):
        return

    dfs(numbers, target, idx+1, values + numbers[idx])
    dfs(numbers, target, idx+1, values - numbers[idx])
=======
def dfs(numbers_list, target, idx, value):
    global answer

    N = len(numbers_list)

    if idx == N:
        if value == target:
            answer += 1
        return

    dfs(numbers_list, target, idx+1, value + numbers_list[idx])
    dfs(numbers_list, target, idx+1, value - numbers_list[idx])
>>>>>>> 18eaa442434aae5d7fc1de0228bbb779e04ff92d


def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers, target, 0, 0)

    return answer

<<<<<<< HEAD
=======

>>>>>>> 18eaa442434aae5d7fc1de0228bbb779e04ff92d
# 5
print(solution([1, 1, 1, 1, 1], 3))

# 2
print(solution([4, 1, 2, 1], 4))
