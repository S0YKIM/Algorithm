def	quick_sort(array, start, end) :
	# 원소가 1개인 경우 종료
	if start >= end :
		return
	# 첫 번째 원소가 피벗
	pivot = start
	left = start + 1
	right = end
	while left <= right :
		# left: 피벗보다 큰 데이터 (왼쪽부터 오른쪽으로 한 칸씩 탐색)
		while left <= end and array[left] <= array[pivot] :
			left += 1
		# right: 피벗보다 작은 데이터 (오른쪽부터 왼쪽으로 한 칸씩 탐색)
		while right > start and array[right] >= array[pivot] :
			right -= 1
		# left/right 가 엇갈렸다면 right(작은 데이터)와 피벗을 교체
		if left > right :
			array[right], array[pivot] = array[pivot], array[right]
		# left/right 가 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
		else :
			array[left], array[right] = array[right], array[left]
	# 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
	quick_sort(array, start, right - 1)
	quick_sort(array, right + 1, end)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(array, 0, len(array) - 1)
print(array)
