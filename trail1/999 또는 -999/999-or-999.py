arr = tuple(map(int, input().split()))

min = arr[0]

for i in arr[1::]:
    if i == 999 or i == -999:
        break
    
    if min > i:
        min = i

max = arr[0]
for i in arr[1::]:
    if i == 999 or i == -999:
        break
    
    if max < i:
        max = i

print(max, min)