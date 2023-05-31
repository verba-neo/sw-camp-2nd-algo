from itertools import permutations

def solution(k, dungeons):
    answer = 0

    sunsu = []
    for p in permutations(dungeons):
        sunsu.append(p)
    print(sunsu)

    max_go_in = 0
    for s in sunsu:
        pirodo = k
        go_in = 0
        for dungeon in s:
            print(pirodo, dungeon)
            necessary_k = dungeon[0]
            waste_k = dungeon[1]
            if necessary_k <= pirodo:
                pirodo -= waste_k
                go_in += 1
            else:
                break

        if go_in > max_go_in:
            max_go_in = go_in

    return max_go_in


# def solution2(k, dungeons):
#     answer = 0
#
#     dun_len = len(dungeons)
#     visited = [False for _ in range(dun_len)]     # 던전 길이만큼. 각 던전의 방문을 조회해야하므로. 한 조합에서 재방문 X.
#
#     def my_permutation():
#
#
#
#     return answer


input_k = 80
input_dungeons = [[80, 20], [50, 40], [30, 10]]
print(solution(input_k, input_dungeons))
print(solution2(input_k, input_dungeons))