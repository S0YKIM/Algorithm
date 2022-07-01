### 덱
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1) # 덱의 앞에 삽입 (스택이나 큐에선 사용 X)
data.append(5) # 덱의 뒤에 삽입 (스택, 큐 공통)
data.popleft() # 덱의 앞에 있는 원소 제거 (큐)
data.pop() # 덱의 뒤에 있는 원소 제거(스택)

print(data)
print(list(data)) # 리스트형으로 변환


### 카운터
from collections import Counter

array = ['red', 'blue', 'red', 'green', 'blue', 'blue']
counter = Counter(array)

print(counter['blue'])
print(counter)
print(dict(counter)) # 딕셔너리형으로 변환
