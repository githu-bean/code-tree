n, m = map(int, input().split())

# Please write your code here.
arr = [ [0 for _ in range(m)] for _ in range(n) ]

value = 0

for j in range(m):
    if j % 2 == 0:
        for i in range(n):
            arr[i][j] = value
            value += 1
    else:
        for i in range(n-1, -1, -1):
            arr[i][j] = value
            value += 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()