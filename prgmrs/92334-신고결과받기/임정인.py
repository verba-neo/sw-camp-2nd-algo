def solution(id_list, report, k):
    reported_cnt = {x: 0 for x in id_list}  # 모든 id_list 0으로 초기화
    received_mail_cnt = [0] * len(id_list)  # id_list 길이만큼 리스트 0으로 초기화

    # 한 명이 여러번 신고해도 1번의 신고로 인정하므로 중복 불가능 (set)
    for r in set(report):  # report 형식 : '이용자id 신고한id'
        reported_cnt[r.split()[1]] += 1

    for r in set(report):
        if reported_cnt[r.split()[1]] >= k:  # k번 이상 신고 당하면 (2, 3)
            received_mail_cnt[id_list.index(r.split()[0])] += 1

    return received_mail_cnt


# [2,1,1,0]
print(
    solution(
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
        2
    )
)

# [0,0]
print(
    solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)
)
