A = [
	[1, 0, 0, 0],
	[1, 0, 0, 0],
	[1, 0, 0, 0],
	[1, 0, 0, 0]
]

B = [
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 0, 0]
]

array = list()
for i in range(len(A)) :
	array.append(list())
	array[i].append(A[i])
	array[i].append(B[i])
print(array)
