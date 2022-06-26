# 공간의 크기
size = int(input())
# 계획서 내용
directions = list(input().split())
# 여행가의 위치(세로 방향, 가로 방향)
pos = [1, 1]
# 이동 방향
types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for direction in directions :
	for i in range(len(types)) :
		if types[i] == direction :
			nx = pos[0] + dx[i]
			ny = pos[1] + dy[i]
			break
	if nx < 1 or nx > size or ny < 1 or ny > size :
		continue
	pos[0], pos[1] = nx, ny
print(pos[0], pos[1])
