# id_list => 이용자의 id가 담긴 문자열 배열
# repot => 각 이용자가 신고한 이용자의 id정보
# k => 정지 기준이 되는 신고 횟수
# 각 유저 별로 처리결과 메일을 받은 횟수를 배열에 담아 return
# 신고 중복 x

# 메일을 보내려면 무엇이 필요할까?
# k회 이상 신고 받은 목록
# 정지 당한 사람을 신고한 사람의 목록


def solution(id_list, report, k):
    answer = [0]*len(id_list)

    # 신고 중복 x
    report = list(set(report))

    # 신고한 사람: 신고당한 사람 dict
    sue = {}

    # 신고 당한 사람: 신고 횟수 dict
    count = {}

    for elem in report:
        name, reported = elem.split()
        # 신고한 사람: 신고 당한 사람 추가
        if name not in sue:
            sue[name] = [reported]
        else:
            sue[name] += [reported]

        # 신고당한 사람: 신고 횟수 count 추가
        if reported not in count:
            count[reported] = 1
        else:
            count[reported] += 1
    # count의 신고당한 사람과 count를 체크
    for _id, cnt in count.items():
        # k회 이상 신고 받았을 경우
        if cnt >= k:
            # sue의 신고한 사람과 신고당한 사람을 순회하면서
            for name, reported in sue.items():
                # 신고당한 사람의 아이디가 있으면
                if _id in reported:
                    # 신고한 사람의 아이디에 1회 추가
                    answer[id_list.index(name)] += 1

    return answer

# def solution(id_list, report, k):
#     answer = [0]*len(id_list)
#
#     # 중복제거
#     report = list(set(report))
#     #print(report)
#
#     # 신고받은 사람과  신고 받은 횟수
#     name_count = {name : 0 for name in id_list}
#     # print(reports)
#
#     # 신고 받은 사람이 있으면 받은 횟수 +1
#     for reported in report:
#         name_count[reported.split()[1]] += 1
#     # k번 이상 신고받은 사람의 신고 횟수 + 1
#     for reported in report:
#         if name_count[reported.split()[1]] >= k:
#             answer[id_list.index(reported.split()[0])] += 1
#
#     return answer



# [0,0]
print(
    solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)
)

print(
    solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
)