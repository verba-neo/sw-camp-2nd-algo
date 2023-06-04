def solution(numbers, target):
    N = len(numbers)
    answer = 0

    def dfs(idx, result):
        nonlocal answer
        # idx 값이 N이거나, 결과가 타겟과 같다면 answer + 1을 해준다.
        if idx == N:
            if result == target:
                answer += 1
            return
        else:
            dfs(idx+1, result + numbers[idx])
            dfs(idx+1, result - numbers[idx])


    dfs(0, 0)
    return answer


# 5
print(solution([1, 1, 1, 1, 1], 3))
# 2
print(solution([4, 1, 2, 1], 4))
