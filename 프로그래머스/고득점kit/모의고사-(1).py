from collections import defaultdict

def get_one_answer(total) :
    repeated_set = [1, 2, 3, 4, 5]
    # 반복되는 세트의 길이
    length = len(repeated_set)
    # 세트 반복 횟수
    quotient = total // length
    # 세트 반복 후에 남는 횟수
    remainder = total % length
    answer = list()
    for _ in range(quotient) :
        answer.extend(repeated_set)
    for i in range(remainder) :
        answer.append(repeated_set[i])
    return answer

def get_two_answer(total) :
    repeated_set = [2, 1, 2, 3, 2, 4, 2, 5]
    length = len(repeated_set)
    quotient = total // length
    remainder = total % length
    answer = list()
    for _ in range(quotient) :
        answer.extend(repeated_set)
    for i in range(remainder) :
        answer.append(repeated_set[i])
    return answer

def get_three_answer(total) :
    repeated_set = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    length = len(repeated_set)
    quotient = total // length
    remainder = total % length
    answer = list()
    for _ in range(quotient) :
        answer.extend(repeated_set)
    for i in range(remainder) :
        answer.append(repeated_set[i])
    return answer

def get_who_got_highest_score(one, two, three, answers) :
    scores = defaultdict(int)
    for i, answer in enumerate(answers) :
        if one[i] == answer :
            scores['one'] += 1
        if two[i] == answer :
            scores['two'] += 1
        if three[i] == answer :
            scores['three'] += 1
    answer = list()
    maxscore = max(scores.values())
    for person, score in scores.items() :
        if score == maxscore :
            answer.append(person)
    return answer

def replace_eng_with_num(answer) :
    new = list()
    for i in answer :
        if i == 'one' :
            new.append(1)
        elif i == 'two' :
            new.append(2)
        elif i == 'three' :
            new.append(3)
    new.sort()
    return new
    
def solution(answers):
    total = len(answers)
    one = get_one_answer(total)
    two = get_two_answer(total)
    three = get_three_answer(total)
    answer = get_who_got_highest_score(one, two, three, answers)
    answer = replace_eng_with_num(answer)
    return answer
