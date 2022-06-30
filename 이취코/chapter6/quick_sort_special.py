def	quick_sort(array) :
	# 리스트가 하나 이하의 원소만 담고 있다면 종료
	if len(array) <= 1 :
		return array
	# 첫 번째 원소가 피벗
	pivot = array[0]
	# 피벗을 제외한 리스트
	tail = array[1:]

	left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분(피벗보다 작거나 같은 데이터)
	right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분(피벗보다 큰 데이터)

	# 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고 전체 리스트를 반환
	return quick_sort(left_side) + [pivot] + quick_sort(right_side)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array = quick_sort(array)
print(array)
