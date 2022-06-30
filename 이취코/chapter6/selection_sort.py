def	selection_sort(array) :
	for i in range(len(array)) :
		min = i
		for j in range(i, len(array)) :
			if array[j] < min :
				min = array[j]
		min_index = array.index(min)
		array[i], array[min_index] = array[min_index], array[i]

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

selection_sort(array)
print(array)
