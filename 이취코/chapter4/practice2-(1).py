# 정수 N 이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수?

N = int(input())
sum = 0

# 초: x3, 3x
sec = 6 + 10 - 1
# 분: x3, 3x
min = 6 + 10 - 1
# 시: N > 2 이면 03시, N > 12 이면 03, 13시
if N < 3 :
	hour = 0
elif N >= 3 and N < 13 :
	hour = 1
else :
	hour = 2 

# 초에 3이 들어간 경우
sum += sec * 60 * (N + 1)
# 분에 3이 들어간 경우
sum += min * 60 * (N + 1)
# 시에 3이 들어간 경우
sum += hour * 60 * 60
# 겹치게 센 것 빼주기
sum -= (sec * min * (N + 1) + sec * hour * 60 + min * hour * 60)
# 너무 많이 뺀 것 다시 더하기
sum += sec * min * hour
print(sum)
