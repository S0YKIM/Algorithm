import sys

score = int(sys.stdin.readline())

# 딕셔너리 응용
def get_grade_alphabet(score):
    if score <= 5:
        print('F')
    gradebook = { 10 : 'A', 9 : 'A', 8 : 'B', 7 : 'C', 6 : 'D'}.get(score, "")
    print(gradebook)
get_grade_alphabet(score//10)


# # 숏코딩
# print('FFFFFFDCBAA'[score//10])


# #정석
# if 90 <= score and score <= 100:
#     print("A")
# elif 80 <= score and score < 90:
#     print("B")
# elif 70 <= score and score < 80:
#     print("C")
# elif 60 <= score and score < 70:
#     print("D")
# else:
#     print("F")