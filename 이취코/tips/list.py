### 리스트 메서드 사용법

array = [1, 2, 4, 5]
print("-------------------------------")
print(array)
print("-------------------------------")

# 원소 삽입
array.append(3)
print("-------------------------------")
print("Append 3: ")
print(array)
print("-------------------------------")

# 오름차순 정렬
array.sort()
print("-------------------------------")
print("Ascending sort: ")
print(array)
print("-------------------------------")

# 내림차순 정렬
array.sort(reverse = True)
print("-------------------------------")
print("Descending sort: ")
print(array)
print("-------------------------------")

# 리스트 원소 뒤집기
array.reverse()
print("-------------------------------")
print("Reverse list: ")
print(array)
print("-------------------------------")

# 특정 인덱스에 데이터 추가
array.insert(2, 5)
print("-------------------------------")
print("Insert 5: ")
print(array)
print("-------------------------------")

# 특정 값인 데이터 개수 세기
print("-------------------------------")
print("Number of data 5: ", array.count(5))
print("-------------------------------")

# 특정 값인 데이터 삭제
array.remove(5)
print("-------------------------------")
print("Remove 5: ")
print(array)
print("-------------------------------")

# 특정 인덱스에 있는 데이터 삭제
del array[2]
print("-------------------------------")
print("Remove 3: ")
print(array)
print("-------------------------------")
