def solution(id_list, report, k):
    # {신고 당한 사람: [신고한 사람들]}
    reports_dict = {}
    for rep in report:
        user_id, target_id = rep.split()
        if not reports_dict.get(target_id):
            reports_dict.setdefault(target_id, [])
        # 중복 신고 제거
        if user_id not in reports_dict[target_id]:
            reports_dict[target_id] += [user_id]

    mail_count = {}
    for user_id in reports_dict:
        if len(reports_dict[user_id]) >= k:
            # k 이상 신고받은 사람을 찾아서 신고한 사람들 메일 갯수 계산
            for recipient in reports_dict[user_id]:
                if mail_count.get(recipient):
                    mail_count[recipient] += 1
                else:
                    mail_count.setdefault(recipient, 1)

    answer = []
    for user_id in id_list:
        if mail_count.get(user_id):
            answer.append(mail_count[user_id])
        else:
            answer.append(0)

    return answer


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