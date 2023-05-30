def solution(string):
    answer = []
    # dupllist = {}
    # for idx, v in enumerate(string):
    #     count_v = string.count(v)
    #     if count_v >= 2:
    #         if v in dupllist.keys():
    #             dupllist[v].append(idx)
    #         else:
    #             dupllist[v] = [idx]
    #
    # print(dupllist)
    # if dupllist == {}:
    #     return 'N'
    #
    # for k, v in dupllist.items():
    #     # initv = v[-1]
    #     # print( k, v)
    #     # for i in v[:-1]:
    #     #     if initv - i >= 2:
    #     #         answer.append(k)
    #     #         break
    #
    #     for idx in range(len(v) - 1):
    #         # print(v[idx+1] - v[idx])
    #         if v[idx + 1] - v[idx] >= 2:
    #             answer.append(k)
    #             break
    #         else:
    #             idx += 1
    #
    # answer.sort()
    # answer_out = ''
    # for a in answer:
    #     answer_out += a

    idx = 0
    while idx < len(string) - 1:
        if string[idx + 1] == string[idx]:
            idx += 1
        else:
            if string[idx + 1:].count(string[idx]):
                answer.append(string[idx])
            idx += 1

    if not answer:
        return 'N'

    answer_sort = sorted(set(answer))
    answer_out = ''
    for a in answer_sort:
        answer_out += a


    return answer_out