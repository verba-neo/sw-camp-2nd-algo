def solution(id_list, report, k):
    # ?
    answer = []

    # 신고받은 횟수
    spts = {id: set() for id in id_list}

    for i in report:
        rpt, spt = map(str, i.split())
        spts[spt].add(rpt)

    mail = {id: 0 for id in id_list}
    for id in id_list:
        if len(spts[id]) >= k:
            for rpt in spts[id]:
                mail[rpt] += 1
    for i, v in mail.items():
        answer.append(v)
    print(spts)
    print(mail)

    return answer

    # stack 으로 풀어보기



input_id_list = ["muzi", "frodo", "apeach", "neo"]
input_report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
input_k = 2
print(solution(input_id_list, input_report, input_k))
