# 메모이제이션: 한 번 구한 결과는 메모해두고 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오기
memo = [0] * 100

def	fibo(x) :
	if x == 1 or x == 2 :
		return 1
	# 이미 계산한 적이 있다면 그대로 반환
	elif memo[x] != 0 :
		return memo[x]
	memo[x] = fibo(x-1) + fibo(x-2)
	return memo[x]

print(fibo(4))

# 다이나믹 프로그래밍
# 큰 문제를 작게 나눈다
# 한 번 풀었던 문제라면 다시 계산하지 않는다
