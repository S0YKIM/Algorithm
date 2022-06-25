# 행의 개수, 열의 개수
N, M = map(int, input().split())

# 가장 큰 수
result = 0
# N개의 행이 있으므로 N번 순회
for i in range(N) :
	nums = list(map(int, input().split()))
	# 해당 행에서 가장 작은 수
	min_value = min(nums)
	# 이전의 가장 작은 수와 현재의 가장 작은 수 비교하여 더 큰 값을 결과로 저장
	result = max(result, min_value)
print(result)
