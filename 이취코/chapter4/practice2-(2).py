# 정수 N 이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수?

N = int(input())

cnt = 0
for hour in range(N + 1):
	for min in range(60) :
		for sec in range(60) :
			if '3' in str(hour) + str(min) + str(sec) :
				cnt += 1
print(cnt)
