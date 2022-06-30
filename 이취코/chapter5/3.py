# 얼음틀 크기(행 x 열)
N, M = map(int, input().split())

# 얼음틀(0: 구멍이 뚫려 있음, 1: 칸막이로 막혀 있음)
tray = list()
for _ in range(N) :
	tray.append(list(map(int, input())))

def	dfs(x, y) :
	if x < 0 or x >= N or y < 0 or y >= M :
		return False
	if tray[x][y] == 0 :
		tray[x][y] = 1
		dfs(x-1, y)
		dfs(x+1, y)
		dfs(x, y-1)
		dfs(x, y+1)
		return True
	return False

# 총 아이스크림 개수
cnt = 0
for i in range(N) :
	for j in range(M) :
		if dfs(i, j) :
			cnt += 1
print(cnt)
