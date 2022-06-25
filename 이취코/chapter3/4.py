# 1번: N 에서 1 을 빼는 연산
# 2번: N 에서 K 로 나누는 연산
N, K = map(int, input().split())

# 총 연산 횟수
cnt = 0
while N > 1 :
	# 2번 연산
	if N % K == 0 :
		N //= K
	# 1번 연산
	else :
		N -= 1
	cnt += 1
print(cnt)
