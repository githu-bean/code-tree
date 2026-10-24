n = int(input())

arr = [ [0 for _ in range(n+1)] for _ in range(n+1) ]

for i in range(n+1):
    arr[i][0] = 1

for i in range(2, n+1):
    for j in range(1, n+1):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

for i in range(1, n+1):
    for j in range(n+1):
        if arr[i][j] != 0:
            print(arr[i][j], end=' ')
    print()