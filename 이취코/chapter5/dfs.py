#  3 ------  1 - 2 - 7
#  ㅣ \         \   /  \
#  4 - 5         8     6

def	dfs(graph, visited, v) :
	visited[v] = True
	print(v, end=' ')
	for i in graph[v] :
		if not visited[i] :
			dfs(graph, visited, i)

# 주어진 그래프
graph = [
	[],
	[2, 3, 8],
	[1, 7],
	[1, 4, 5],
	[3, 5],
	[3, 4],
	[7],
	[2, 6, 8],
	[1, 7]
]

# 방문한 노드인지 확인
visited = [False] * 9

# 시작 노드
start = 1
dfs(graph, visited, start)
