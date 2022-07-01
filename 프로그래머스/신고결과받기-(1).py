def get_report_without_dup(id_list, report):
    result = list()
    for i in id_list :
        result.append([i])
    for i in range(len(result)) :
        for j in report :
            reporter, reported = j.split()
            if result[i][0] == reporter and reported not in result[i] :
                result[i].append(reported)
    return result

def get_report_banned_people(id_list, new_report, k):
    ban_report = list()
    count = dict()
    for i in new_report :
        for j in range(1, len(i)) :
            reported = i[j]
            count[reported] = count.get(reported, 0) + 1
    for person, cnt in count.items() :
        if cnt >= k :
            ban_report.append(person)
    return ban_report

def get_list_of_mails_count(new_report, ban_report) :
    result = [0] * len(new_report)
    for i in range(len(new_report)) :
        for j in new_report[i][1:] :
            if j in ban_report :
                result[i] += 1
    return result
            
    
def solution(id_list, report, k):
    # 중복 신고가 없는 새로운 신고 리포트 생성
    new_report = get_report_without_dup(id_list, report)
    # 정지된 사람 리스트
    ban_report = get_report_banned_people(id_list, new_report, k)
    # 신고 처리 완료 메일은 받은 횟수
    answer = get_list_of_mails_count(new_report, ban_report)
    return answer
