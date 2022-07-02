# 2차원 리스트를 시계방향으로 90도 회전시키는 코드

def	rotate_matrix_by_90_degree(a) :
	n = len(a) # 행 길이(=새로운 리스트의 열 길이)
	m = len(a[0]) # 열 길이(=새로운 리스트의 행 길이)
	result = [[0] * n for _ in range(m)] # 결과 리스트
	for i in range(n) :
		for j in range(m) :
			result[j][n - i - 1] = a[i][j]
	return result

a = [
	[1, 1, 1],
	[0, 0, 0],
	[1, 0, 1]
]
a = rotate_matrix_by_90_degree(a)
print(a)
