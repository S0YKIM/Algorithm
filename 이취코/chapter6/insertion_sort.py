def	insertion_sort(array) :
	for i in range(1, len(array)) :
		for j in range(i, 0, -1) :
			if array[j] < array[j-1] :
				array[j], array[j-1] = array[j-1], array[j]
			else :
				break # 정렬이 이루어진 원소는 항상 오름차순을 유지하기 때문

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
insertion_sort(array)
print(array)
