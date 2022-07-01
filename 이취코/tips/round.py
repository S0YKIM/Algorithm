# round(a, b)
# a : 실수형 데이터
# b : 반올림하고자 하는 위치 - 1

a = 0.301 + 0.602
result = round(a, 2) # 소수점 셋째 자리에서 반올림
print(result)

if result == 0.9 :
	print(True)
else :
	print(False)
