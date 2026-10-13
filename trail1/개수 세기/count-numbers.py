N, M = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

cnt = 0

for value in arr:
    if value == M:
        cnt += 1

print(cnt)