# # 모두 순열 만들어서 그 중에 최대 던전 수 리턴

from itertools import permutations
# 재귀로 풀어보는 것 추천
def solution(k, dungeons):  # 최소 필요 피로도, 소모피로도
    maxdg = 0  # 최대 돌 수 있는 던전 수
    for dlist in permutations(dungeons, len(dungeons)):  # 순열로 던전 다양한 순서 경험
        first = k  # 최초 체력 (피로도)
        answer = 0  # 각 경우 별 최대 던전 탐험 수
        for dg in dlist:
            if first >= dg[0]:
                first -= dg[1]
                answer += 1
        maxdg = max(maxdg, answer)
    return maxdg

# (2) 강사님 - itertools > permutations 사용
def solution(k, dungeons):
    from itertools import permutations
    N = len(dungeons)
    answer = -1

    # plan => A - B - C 같이 순열 모음에서 하나의 케이스
    for plan in permutations(dungeons):
        # 이번 plan 에서 몇 개를 성공했는지
        count = 0
        # 체력 초기화
        hp = k
        # 각 계획마다 필요한 체력/깎이는 체력
        for require, damage in plan:
            # 현재 남은 hp가 필요량보다 적거나, 지금 hp가 0이 되었다면, 이번 plan은 끝
            if hp < require or hp <= 0:
                break
            # 아니면 도전
            else:
                # 체력 -
                hp -= damage
                # 성공 +1
                count += 1
        # 하나의 순열이 끝나고, 최댓값 갱신
        if count > answer:
            answer = count
        # 갱신한 최댓값이 전체 던전수와 같다면 이게 가장 많은 경우의 수
        if answer == N:
            # 더 볼것 없이 답
            return answer
    # 모든 순열에서 가장 큰 값 return
    return answer


# (3) 강사님 - 재귀(dfs) 구현
def solution(k, dungeons):
    answer = -1
    # 전체 던전 개수
    dungeons_count = len(dungeons)
    # 던전 방문 여부
    visited = [False for _ in range(dungeons_count)]

    def dfs(count, left_hp):
        nonlocal answer

        # 지금까지 클리어한 개수가 최대면
        if count > answer:
            # 갱신
            answer = count

        # 던전 번호 순서대로 순회하되
        for dungeon_idx in range(dungeons_count):
            # 현재 클리어한게 전체 개수랑 같거나, 남은 체력이 없으면 더 볼 필요 없음
            if answer == dungeons_count or left_hp <= 0:
                return

            # 현재 탐험하지 않은 경우에만
            if not visited[dungeon_idx]:
                # 도전(방문)
                visited[dungeon_idx] = True
                require_hp, damage = dungeons[dungeon_idx]
                # 클리어 가능하다면,
                if left_hp >= require_hp:
                    # 클리어 +1, 체력 - 하고 다음 회차로 진행
                    dfs(count+1, left_hp-damage)
                # 클리어하고 다음으로 가던, 클리어 못하던 비방문 처리로 바꿈
                visited[dungeon_idx] = False

    dfs(0, k)
    return answer

print(solution(80, [[80,20], [50,40], [30,10]]))
