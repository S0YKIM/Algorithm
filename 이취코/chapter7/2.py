### 부품 찾기

def	is_it_in_the_store(have, thing, start, end) :
	if start > end :
		return False
	mid = (start + end) // 2
	if have[mid] == thing :
		return True
	elif have[mid] < thing :
		return is_it_in_the_store(have, thing, mid + 1, end)
	else :
		return is_it_in_the_store(have, thing, start, mid - 1)


N = int(input()) # 매장에 가지고 있는 부품 개수
have = list(map(int, input().split())) # 매장에 있는 부품 번호 리스트
M = int(input()) # 손님이 찾는 부품 개수
need = list(map(int, input().split())) # 손님이 찾는 부품 번호 리스트

have.sort()
for i in need :
	result = is_it_in_the_store(have, i, 0, len(have) - 1)
	if result :
		print("yes", end=' ')
	else :
		print("no", end=' ')
