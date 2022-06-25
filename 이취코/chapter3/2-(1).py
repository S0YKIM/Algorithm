# 배열의 크기, 더하는 횟수, 연속 더하기 제한 횟수
size, add, limit = map(int, input().split())
array = list(map(int, input().split()))
sum = 0

# 가장 큰 수와 두 번째로 큰 수
first = max(array)
array.remove(first)
second = max(array)

# limit 에 도달했는지 알려주는 플래그
flag = 0
for i in range(add) :
	if flag == limit :
		sum += second
		flag = 0
	else :
		sum += first
		flag += 1
print(sum)
