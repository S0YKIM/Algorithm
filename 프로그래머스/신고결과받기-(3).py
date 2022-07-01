from collections import defaultdict

def solution(id_list, report, k):
    # 중복 신고 제외
    report = set(report)
    # 신고된 횟수 딕셔너리
    count = defaultdict(int)
    # 유저별 신고한 사람 리스트
    whom_i_reported = defaultdict(set)
    # 정지된 사람 리스트
    banned = list()
    
    for i in report :
        reporter, reported = i.split()
        whom_i_reported[reporter].add(reported)
        count[reported] += 1
        if count[reported] == k :
            banned.append(reported)
    
    # 신고 처리 완료 메일을 받은 횟수 리스트
    answer = [0] * len(id_list)
    for i in banned :
        for j in range(len(id_list)) :
            if i in whom_i_reported[id_list[j]] :
                answer[j] += 1
    return answer
