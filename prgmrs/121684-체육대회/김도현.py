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

def my_permutation():
    
    return

def solution2(ability):
    answer = 0



    return answer


input_ability = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]
# input_ability = [[20, 30], [30, 20], [20, 30]]
print(solution(input_ability))
print(solution2(input_ability))
