N = int(input())

arr = [1, N] + [0] * 98

for i in range(2, 100):
    arr[i] = arr[i-2] + arr[i-1]
    if arr[i] > 100:
        break

for i in [j for j in arr if j > 0]:
    print(i, end=' ')