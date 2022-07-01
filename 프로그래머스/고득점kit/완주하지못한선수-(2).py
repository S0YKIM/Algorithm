from collections import Counter

def solution(participant, completion):
    count = Counter(completion)
    for i in participant :
        if i not in count :
            return i
        elif count[i] == 0 :
            return i
        else :
            count[i] -= 1
    return ''
