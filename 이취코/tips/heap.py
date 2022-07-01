# 힙을 이용하여 힙 정렬 구현

import heapq

def	heapsort(iterable) :
	h = []
	result = []
	for i in iterable :
		heapq.heappush(h, i) # heappush : 힙 불변성을 유지하면서 주어진 값을 힙에 추가
	for _ in range(len(h)) :
		result.append(heapq.heappop(h)) # heappop : 힙에서 가장 작은 원소를 제거하고 반환
	return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
