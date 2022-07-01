from bisect import bisect_left, bisect_right

# -------------------------------------------------
# 기본적인 메서드 사용법
# -------------------------------------------------
array = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(array, x)) # 정렬된 순서를 유지하면서 리스트에 데이터 x 를 삽입할 가장 왼쪽 인덱스를 찾음
print(bisect_right(array, x)) # 정렬된 순서를 유지하면서 리스트에 데이터 x 를 삽입할 가장 오른쪽 인덱스를 찾음


# -------------------------------------------------
# 특정 범위에 속하는 원소의 개수 찾기
# -------------------------------------------------

def	count_by_range(a, left_value, right_value) :
	left_index = bisect_left(a, left_value)
	right_index = bisect_right(a, right_value)
	cnt = right_index - left_index
	return cnt

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4)) # 값이 4인 데이터 개수
print(count_by_range(a, -1, 3)) # 값이 [-1, 3] 범위에 있는 데이터 개수
