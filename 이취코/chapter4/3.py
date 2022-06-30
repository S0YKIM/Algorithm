def	is_move_available(nx, ny, size, tiles) :
	if nx < 0 or nx > size[1] or ny < 0 or ny > size[0] :
		return False
	elif tiles[ny][nx] == 1 or tiles[ny][nx] == -1 :
		return False
	else :
		return True

def	move(pos, tiles, size) :
	type = [0, 1, 2, 3]
	dx = [0, 1, 0, -1]
	dy = [-1, 0, 1, 0]
	for i in type :
		if pos[2] == i :
			ny = pos[0] + dy[i]
			nx = pos[1] + dx[i]
	if is_move_available(nx, ny, size, tiles) : 
		# 새로운 위치 가본 곳으로 표시
		tiles[ny][nx] = -1
		# 위치 업데이트
		pos[0] = ny
		pos[1] = nx
		return True
	else :
		return False

def	move_back(pos, tiles) :
	type = [0, 1, 2, 3]
	dx = [0, 1, 0, -1]
	dy = [-1, 0, 1, 0]
	for i in type :
		if pos[2] == i :
			ny = pos[0] - dy[i]
			nx = pos[1] - dx[i]
	# 뒤가 바다이면 종료
	if tiles[ny][nx] == 1 :
		return False
	# 위치 업데이트
	pos[0] = ny
	pos[1] = nx
	return True

def turn_left(pos) :
	if pos[2] == 0 :
		pos[2] = 4
	pos[2] -= 1

# 맵의 크기(세로x가로)
size = list(map(int, input().split()))

# 캐릭터의 위치와 바라보는 방향(수직 방향, 수평 방향, 동서남북(0[북], 1[동], 2[남], 3[서]))
pos = list(map(int, input().split()))

# 맵의 타일이 육지인지 바다인지(0[육지], 1[바다])
tiles = list()
for _ in range(size[0]) :
	tiles.append(list(map(int, input().split())))

# 현재 위치 가본 곳으로 표시
tiles[pos[0]][pos[1]] = -1

# 이동 횟수와 왼쪽으로 회전한 횟수
move_count = 1
turn_count = 0

# 종료 플래그(False 면 종료)
flag = True
while flag :
	turn_left(pos)
	if move(pos, tiles, size) :
		move_count += 1
		turn_count = 0
		# print(pos)
	else :
		turn_count += 1
		# print(pos)
	if turn_count == 4 :
		flag = move_back(pos, tiles)
		turn_count = 0
		# print(pos)
print(move_count)
