def get_count_of_reported(report) :
    count = dict()
    for i in report :
        reporter, reported = i.split()
        count[reported] = count.get(reported, 0) + 1
    return count

def get_banned_list(count, k) :
    banned = list()
    for person, cnt in count.items() :
        if cnt >= k :
            banned.append(person)
    return banned

def get_list_of_mails_count(id_list, report, banned) :
    answer = [0] * len(id_list)
    index = 0
    for i in id_list :
        for j in report :
            reporter, reported = j.split()
            if i == reporter and reported in banned :
                answer[index] += 1
        index += 1
    return answer

def solution(id_list, report, k):
    # 중복 신고 제외
    report = set(report)
    # 신고된 사람과 횟수를 담은 딕셔너리
    count = get_count_of_reported(report)
    # 정지된 유저 리스트
    banned = get_banned_list(count, k)
    # 신고 처리 완료 메일을 받은 횟수를 담은 리스트
    answer = get_list_of_mails_count(id_list, report, banned)
    return answer
