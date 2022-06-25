# 아이디어: 각 행의 숫자 중에서 최소인 숫자들을 모아 가장 큰 숫자를 고른다

# 행의 개수, 열의 개수
N, M = map(int, input().split())

# 카드 숫자 2차원 배열
cards = list()
for i in range(N) :
	cards.append(list(map(int, input().split())))

# 각 행에서 가장 작은 수들의 리스트
mins = list()
for i in range(N) :
	mins.append(min(cards[i]))

# 가장 작은 수들의 모임 중에서 가장 큰 숫자를 고른다
print(max(mins))
