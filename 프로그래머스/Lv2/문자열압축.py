def add_to_new_string(newstring, cnt, prev) :
    if cnt > 1 :
        newstring += str(cnt) + prev
    else :
        newstring += prev
    return newstring

def solution(s):
    # 최대 압축 단위(문자열 길이의 절반이 넘으면 의미 없음)
    mid = len(s) // 2
    # 아무것도 압축할 것이 없는 경우
    answer = len(s)
    for step in range(1, mid + 1) :
        newstring = ''
        prev = s[0:step]
        cnt = 1
        for j in range(step, len(s), step) :
            if prev == s[j:j+step] :
                cnt += 1
            else :
                newstring = add_to_new_string(newstring, cnt, prev)
                prev = s[j:j+step]
                cnt = 1
        newstring = add_to_new_string(newstring, cnt, prev)
        answer = min(answer, len(newstring))

    return answer
