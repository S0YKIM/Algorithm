#  3 ------  1 - 2 - 7
#  ㅣ \         \   /  \
#  4 - 5         8     6

from collections import deque

def	bfs(graph, visited, start) :
	# 큐 생성
	queue = deque([start])
	# 시작 노드 방문 처리
	visited[start] = True
	# 큐가 빌 때까지 반복
	while queue :
		v = queue.popleft()
		print(v, end=' ')
		for i in graph[v] :
			if not visited[i] :
				queue.append(i)
				visited[i] = True


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
bfs(graph, visited, start)
