n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
min = a[0]

for i in a[1::]:
    if min > i:
        min = i

cnt = 0

for i in a:
    if min == i:
        cnt += 1

print(min, cnt)