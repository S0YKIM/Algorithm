from bisect import bisect_left, bisect_right

array = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(array, x))
print(bisect_right(array, x))
