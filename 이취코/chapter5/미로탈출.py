from collections import deque

N = 5
M = 6
maze = [
	"101010",
	"111111",
	"000001",
	"111111",
	"111111"
]

def	get_minimum_move(start, end, path) :
	# 동남서북 방향
	dx = [0, 1, 0, -1]
	dy = [1, 0, -1, 0]
	queue = deque()
	queue.append(start)
	while queue :
		pos = queue.popleft()
		for i in range(4) :
			nx = pos[0] + dx[i]
			ny = pos[1] + dy[i]
			if nx < 0 or nx >= N or ny < 0 or ny >= M :
				continue
			elif path[nx][ny] == 0 :
				continue
			elif path[nx][ny] == 1 :
				path[nx][ny] = path[pos[0]][pos[1]] + 1
				queue.append((nx, ny))
	return path[end[0]][end[1]]

def	solution(N, M, maze) :
	path = list()
	for i in range(N) :
		path.append(list(map(int, maze[i])))
	start = (0, 0)
	end = (N - 1, M - 1)
	answer = get_minimum_move(start, end, path)
	return answer

print(solution(N, M, maze))
