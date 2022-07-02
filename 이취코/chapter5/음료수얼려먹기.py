N = 4
M = 5
array = [
	[0, 0, 1, 1, 0],
	[0, 0, 0, 1, 1],
	[1, 1, 1, 1, 1],
	[0, 0, 0, 0, 0]
]


def	dfs(N, M, tray, x, y) :
	if x < 0 or x >= N or y < 0 or y >= M :
		return False
	if tray[x][y] == 0 :
		tray[x][y] = 1
		dfs(N, M, tray, x-1, y)
		dfs(N, M, tray, x+1, y)
		dfs(N, M, tray, x, y-1)
		dfs(N, M, tray, x, y+1)
		return True
	return False


def	solution(N, M, array) :
	answer = 0
	tray = list()
	for i in range(N) :
		tray.append(array[i])
	for i in range(N) :
		for j in range(M) :
			if dfs(N, M, tray, i, j) :
				answer += 1
	return answer

print(solution(N, M, array))
