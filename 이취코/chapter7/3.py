### 떡볶이 떡 만들기

def	get_sum_of_length(ricecakes, mid) :
	sum = 0
	for i in ricecakes :
		if i > mid :
			sum += i - mid
	return sum


def	get_maximum_height(ricecakes, start, end, M) :
	# 절단기의 최대 높이
	max = 0
	while start <= end :
		mid = (start + end) // 2
		# 현재 절단기 높이에서 얻게 되는 떡의 길이의 합
		sum = get_sum_of_length(ricecakes, mid)
		# 떡이 모자라면 절단기 높이 줄이기
		if sum < M :
			end = mid - 1
		# 떡이 충분하면 절단기 높이 올려보기
		else :
			max = mid
			start = mid + 1
	return max


# 매장의 떡의 개수, 요청한 떡의 길이
N, M = map(int, input().split())
# 떡의 개별 길이
ricecakes = list(map(int, input().split()))

max = get_maximum_height(ricecakes, 0, max(ricecakes), M)
print(max)
