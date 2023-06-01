# set 으로 처리
# 모든 종류의 보석을 적어도 1개 이상을 포함하는 가장 짧은 구간
# 시작 진열 번호가 더 작은 값을 return
# 전부를 포함하는 값이 유일하면 전부를 return

# def solution(gems):
#
#     # 1 unique_count = len(set(gems[start:end]))
#     # 2 minimus > len(gems[start:end])
#
#     size = len(set(gems))  # 4  : 4개씩 보기 시작해서 개수 늘려가기
#     idx = []
#     answer = []  # 정답 저장해서 조건을 만족하는 가장 길이가 짧은 수 idx 도출
#
#     # start for 문, end for 문
#     for start in range(len(gems)-size):  # 0:4  idx = 0 1 2 3
#         for end in range(len(gems)-size-1,len(gems)+1):   # 8-4-1 : idx = 3 4 5 6 7
#             if end - start >= 3:  # 오잉 범위가 이상해..
#                 # 만약 해당 범위에서 단어가 다 포함되면
#                 if set(gems) in gems[start:end]:
#                     # answer 에 추가
#                     answer += gems[start:end]
#                 # 단어가 포함되지 않으면
#                 else:
#                     continue
#             else:
#                 continue
#
#             print(start, end)

# 강사님 : 현재 코드 시간 복잡도 = for문 2개만 보면 됨, (N-x)*(N-x) 대략= N^2 (N^2이 압도적으로 크기 때문에)
def solution(gems):
    N = minimum = len(gems)  # 전체 개수 = 현재 최소값
    uniq_count = len(set(gems))
    answer = [1, N]
    for start in range(0, N-uniq_count+1):  # 8-4+1 , 0:5
        for end in range(start+uniq_count, N+1):
            my_gems = gems[start:end]

            if len(set(my_gems)) == uniq_count and len(my_gems) < minimum:
                minimum = len(my_gems)
                answer[0] = start+1
                answer[1] = end
                break

    return answer


#            1 2 3 4 5 6 7 8
#            A B B A A C D A
# start      s s s                조건 만족하는 start 지점 찾기
# end        e e e e e e e        end 먼저 출발
# 시간 복잡도 2N (start N + end N = 2N) => answer = [3,7]
# 딕셔너리 하나 만들기
# len(dictionary) = 4 인 구간 기억 : value = 0 되는 구간 구하기

# (2) 시간 복잡도 줄이기 : 위의 개념을 바탕으로 구현
# def solution(gems):

    # e 는 처음부터 끝까지 감
    # 없으면 추가, 있으면 += 1 : dictionary


# [3, 7]
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# [1, 3]
print(solution(["AA", "AB", "AC", "AA", "AC"]))
# [1, 1]
print(solution(["XYZ", "XYZ", "XYZ"]))
# [1, 5]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))