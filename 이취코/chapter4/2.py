# 현재 나이트의 위치(수평방향, 수직방향)
pos = list(input())
# 계산 편의상 알파벳 숫자로 치환(예: a1 -> 11)
pos[0] = str(ord(pos[0]) - 96)
pos = list(map(int, pos))

# 이동 타입
type = ['UL', 'UR', 'RU', 'RD', 'DL', 'DR', 'LU', 'LD']
# 수평방향 이동
dx = [-1, 1, 2, 2, -1, 1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, 1, -1]

count = 0
for i in range(len(type)) :
	nx = pos[0] + dx[i]
	ny = pos[1] + dy[i]
	if nx < 1 or nx > 8 or ny < 1 or ny > 8 :
		continue
	count += 1
print(count)
