def	move(size, pos, direction) :
	if direction == 'R' and pos[1] < size :
		pos[1] += 1
	elif direction == 'L' and pos[1] > 0 :
		pos[1] -= 1
	elif direction == 'U' and pos[0] > 1 :
		pos[0] -= 1
	elif direction == 'D' and pos[0] < size :
		pos[0] += 1	

# 공간의 크기
size = int(input())
# 계획서 내용
directions = list(input().split())
# 여행가의 위치
pos = [1, 1]

for direction in directions :
	move(size, pos, direction)
print(pos[0], pos[1])
