from itertools import permutations

def solution(ability):
    jongmok_su = len(ability[0])
    sunyul = [p for p in permutations(ability, jongmok_su)]

    max_score = 0
    for sy in sunyul:
        score = 0
        for idx in range(jongmok_su):
            score += sy[idx][idx]

        # print(score)
        if score > max_score:
            max_score = score
    return max_score


# 재귀로 풀어보기

def solution2(ability):
    answer = 0
    student_count = len(ability)
    sport_count = len(ability[0])
    visited = [False for _ in range(student_count)]

    def my_permutation(sport_idx, total):
        nonlocal answer
        if sport_idx == sport_count:
            if total > answer:
                answer = total
            return

        for student_idx in range(student_count):
            if not visited[student_idx]:
                visited[student_idx] = True
                print(sport_idx, total, ability[student_idx][sport_idx])
                # 혹여나 sport 에 모두 채워넣어서(sport_idx == sport_count) answer 을 반환해야할 수도 있으니
                # total 을 계산해서 보내줘야합니다. 거기서 answer 을 total 로 맞춰서 dfs 를 끝내면 answer 이 최신 값으로 새로고칩 됩니다.
                my_permutation(sport_idx+1, total+ability[student_idx][sport_idx])
                visited[student_idx] = False
        return

    my_permutation(0, 0)

    return answer


input_ability = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]
# input_ability = [[20, 30], [30, 20], [20, 30]]
print(solution(input_ability))
print(solution2(input_ability))
