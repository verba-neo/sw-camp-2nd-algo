# itertools > permutations 사용
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


# 3
print(solution(80, [[80, 20], [50, 40], [30, 10]]))


# 재귀(dfs) 구현
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


# 3
print(solution(80, [[80, 20], [50, 40], [30, 10]]))












