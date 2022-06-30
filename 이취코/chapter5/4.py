from collections import deque

# 미로의 크기(행x열)
N, M = map(int, input().split())

# 이동 방향(동, 서, 남, 북)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 미로 정보(0: 괴물 있음, 1: 괴물 없음)
maze = list()
for i in range(N) :
	maze.append(list(map(int, input())))

def	bfs(start, end) :
	# 큐 생성
	queue = deque()
	queue.append(start)
	while queue :
		x, y = queue.popleft()
		# 동서남북 순으로 이동 가능한지 확인
		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]
			# 맵을 벗어난 경우 무시
			if nx < 0 or nx >= N or ny < 0 or ny >= M :
				continue
			# 괴물이 있는 경우 무시
			elif maze[nx][ny] == 0 :
				continue
			# 이동 가능한 경우 최소 이동 횟수 업데이트
			elif maze[nx][ny] == 1 :
				maze[nx][ny] = maze[x][y] + 1
				queue.append((nx, ny))
	return maze[end[0]][end[1]]

# 시작 위치와 종료 위치
start = (0, 0)
end = (N-1, M-1)
print(bfs(start, end))
