def	binary_search(array, target, start, end) :
	# 타겟을 찾을 수 없음
	if start > end :
		return None
	mid = (start + end) // 2
	# 타겟을 찾은 경우 현재 인덱스를 반환
	if array[mid] == target :
		return mid
	# 타겟보다 인덱스가 작은 경우, 오른쪽 탐색
	elif array[mid] < target :
		return binary_search(array, target, mid + 1, end)
	# 타겟보다 인덱스가 큰 경우, 인덱스 왼쪽을 탐색
	else :
		return binary_search(array, target, start, mid - 1)


array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = int(input())
index = binary_search(array, target, 0, len(array) - 1)
if index is None :
	print("%i is not in the array." % target)
else :
	print(index)
