# 배열의 크기, 더하는 횟수, 연속 더하기 제한 횟수
size, add, limit = map(int, input().split())
array = list(map(int, input().split()))

# 가장 큰 수와 두 번째로 큰 수
array.sort(reverse=True)
first = array[0]
second = array[1]

# 가장 큰 수가 더해지는 횟수
cnt = add // (limit + 1) * limit
cnt += add % (limit + 1)

sum = 0
# 가장 큰 수 더하기
sum += first * cnt
# 두 번째로 큰 수 더하기
sum += second * (add - cnt)
print(sum)


# 예를 들어, 입력값이
# 5 8 3
# 2 4 5 4 6
# 이었다면, 가장 큰 수가 6, 두 번째로 큰 수가 5 이므로
# (6 + 6 + 6 + 5) + (6 + 6 + 6 + 5) + ... 가 반복된다는 점을 이용
