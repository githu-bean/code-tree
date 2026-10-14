arr = tuple(map(int, input().split()))

max = arr[0]

for i in arr[1::]:
    if max < i:
        max = i

print(max)