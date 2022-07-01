# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [x for x in range(20) if x % 2 == 1]
print(array)

# N x M 크기의 2차원 리스트 초기화
N = 3
M = 4
array = [[0] * M for _ in range(N)]
print(array)

# 특정한 값의 원소를 리스트에서 모두 제거하기
# 기존 리스트에서 제거를 하는 것이 아니라, 그것을 제외한 새로운 리스트를 만들어 반환!
array = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [x for x in array if x not in remove_set]
print(result)
