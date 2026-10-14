N = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for _ in range(N):
    for i in range(N-1):
        if arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
                
print(arr[0], arr[1])