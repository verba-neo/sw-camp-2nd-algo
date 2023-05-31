def solution(k, dungeons):
    answer = -1

    dungeon_len = len(dungeons)
    stack = []

    for idx in range(dungeon_len):
        if dungeons[idx][0] <= k:   # 입장 가능한 던전만 스택에 포함
            stack.append([k-dungeons[idx][1], idx])

    while stack:
        current = stack.pop()
        k_remain = current[0]      # 남은 피로도
        cnt = len(current)-1       # 방문 횟수
        answer = max(answer, cnt)  # 최대 방문 횟수 갱신

        if cnt == dungeon_len:  # 갱신 최대 값이 던전 수 와 같으면 탈출
            break
        for i in range(dungeon_len):
            # 방문한 적 없고, 남은 피로도 로 방문 가능한 던전 추가
            if i not in current[1:] and dungeons[i][0] <= k_remain:
                # 소모된 피로도 계산 / 방문 가능한 던전 추가
                tmp = current[:]
                # 피로도
                tmp[0] -= dungeons[i][1]
                tmp.append(i)
                stack.append(tmp)

    return answer


k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]

print(solution(k, dungeons))
