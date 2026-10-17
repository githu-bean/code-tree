n = int(input())
arr = list(map(int, input().split()))

min = 100

for i in range(n):
    for j in range(i+1, n):

        value = arr[i] - arr[j]

        if value > 0 and min > value:
            min = value

        elif value < 0 and min > -value:
            min = -value
            
print(min)