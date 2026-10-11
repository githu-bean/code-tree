N = int(input())
arr = list(map(int, input().split()))

for i in [j for j in arr if j % 2 == 0]:
    print(i, end=' ')