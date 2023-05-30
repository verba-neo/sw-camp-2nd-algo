# def permutation_dungeons(dungeons):
#     if len(dungeons) == 1:
#         return [dungeons]
#
#     permutation_list = []
#     for i in range(len(dungeons)):
#         d = dungeons[i]
#
#         remaining_ds = dungeons[:i] + dungeons[i+1:]
#
#         for item in permutation_dungeons(remaining_ds):
#             permutation_list.append([d] + item)
#
#     return permutation_list
#
# def solution(k, dungeons):
#     permutation_dungeons_list = permutation_dungeons(dungeons)
#
#     count_list = []
#     for p_dungeons in permutation_dungeons_list:
#         hp = k
#         count = 0
#         for d in p_dungeons:
#             if hp >= d[0]:
#                 count += 1
#                 hp -= d[1]
#             else:
#                 break
#         count_list.append(count)
#
#         if count == len(dungeons):
#             break
#
#     answer = max(count_list)
#
#     return answer

def solution(k, dungeons):
    answer = -1
    visited = [False for _ in range(len(dungeons))]

    def dfs(dungeon_i, count, hp):
        nonlocal answer

        if count > answer:
            answer = count

        for i in range(len(dungeons)):
            if answer == len(dungeons) or hp <= 0:
                return
            if not visited[i]:
                visited[i] = True
                if hp >= dungeons[i][0]:
                    dfs(dungeon_i + 1, count + 1, hp - dungeons[i][1])
                visited[i] = False

    dfs(0, 0, k)
    return answer


# 3
print(solution(80, [[80,20],[50,40],[30,10]]))
