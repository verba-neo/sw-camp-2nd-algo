def solution(id_list, report, k):

    report_sp = []
    for report_cnt in set(report):
        report_sp.append(report_cnt.split())
    # print(report_sp)

    id_dic = {id_ck: 0 for id_ck in id_list}
    re_dic = {re_cnt: [] for re_cnt in id_list}

    for reporter, reported in report_sp:
        re_dic[reported].append(reporter)

    for id_key in re_dic.keys():
        if len(re_dic[id_key]) >= k:
            for value in re_dic[id_key]:
                id_dic[value] += 1

    answer = []
    for cnt in id_dic.values():
        answer.append(cnt)

    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
print(solution(id_list, report, 2))
