# global 변수들
answer = 0
N = 0
visited = []


def dfs(k, dungeons, count):
    global answer
    # 최대방문횟수
    if count > answer:
        answer = count
    # dfs로 방문 설정
    for i in range(N):
        # 피로도가 최소피로도보다 크거나 같고, 방문하지 않았을 때
        if k >= dungeons[i][0] and not visited[i]:
            # 방문으로 바꿔준다
            visited[i] = True
            # 그리고 다시 dfs 이어가면서 카운트 늘려주기
            dfs(k - dungeons[i][1], dungeons, count+1)
            # 끝까지 가고 나서 다시 방문 초기화
            visited[i] = False


def solution(k, dungeons):
    global N, visited
    # 던전의 갯수 만큼
    N = len(dungeons)
    # False로 다 채워주고
    visited = [False for _ in range(N + 1)]
    # 재귀함수 돌려주기
    dfs(k, dungeons, 0)

    return answer


print(solution(
    80, [[80,20],[50,40],[30,10]]
))
