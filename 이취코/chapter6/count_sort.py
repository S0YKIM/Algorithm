def	count_sort(array) :
	# 모든 범위를 포함하는 리스트 선언
	count = [0] * (max(array) + 1)
	for i in array :
		count[i] += 1
	result = list()
	# 카운트된 개수만큼 인덱스를 반환할 리스트의 요소로 추가
	for i, cnt in enumerate(count) :
		for _ in range(cnt) :
			result.append(i)
	return result

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
result = count_sort(array)
print(result)

# 계수정렬은 특정한 조건이 부합할 때에만 사용 가능!
# 1. 데이터의 크기 범위가 제한되어 있음
# 2. 모든 데이터가 정수 형태로 표현됨
