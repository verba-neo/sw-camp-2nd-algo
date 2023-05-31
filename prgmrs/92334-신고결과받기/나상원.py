def solution(id_li, repo, k):
    
    # set()으로 중복 제거/ 신고자 /신고 대상 split()으로 분리
    report_sp = []
    for report_cnt in set(report):
        report_sp.append(report_cnt.split())
    # print(report_sp)
    
    # id 별로 신고 처리 결과 '0'으로 초기화
    id_dic = {id_ck: 0 for id_ck in id_list}
    
    # 신고 대상을 key 값/ 신고자 는 다수가 있어야 하므로 value list 로 초기화 
    re_dic = {re_cnt: [] for re_cnt in id_list}
    
    # 신고 된 사람을 key 값으로 하는 dic 에 내용 추가
    for reporter, reported in report_sp:
        re_dic[reported].append(reporter)

    # 신고자 가 k 값 이상 이면 처리 결과에 '1'을 더해줌
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
