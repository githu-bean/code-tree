N = list(map(int, input().split()))

arr = [0] * 10

arr[0] = N[0]; arr[1] = N[1]

tmp = 0

for i in range(2, 10):
    tmp = arr[i-2] + arr[i-1]
    
    if tmp >= 10:
        tmp -= 10
    
    arr[i] = tmp

for i in arr:
    print(i, end=' ')