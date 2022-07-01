# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [x for x in range(20) if x % 2 == 1]
print(array)

# N x M 크기의 2차원 리스트 초기화
N = 3
M = 4
array = [[0] * M for _ in range(N)]
print(array)
