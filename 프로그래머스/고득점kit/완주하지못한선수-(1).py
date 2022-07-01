def solution(participant, completion):
    count = {x : 0 for x in completion}
    for i in completion :
        count[i] += 1
    for i in participant :
        if i not in count :
            return i
        elif count[i] == 0 :
            return i
        else :
            count[i] -= 1
    return ''
