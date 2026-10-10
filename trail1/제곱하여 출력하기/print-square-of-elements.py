N = int(input())
arr = list(map(int, input().split()))

for i in [j**2 for j in arr]:
    print(i, end=' ')