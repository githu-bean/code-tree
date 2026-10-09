arr = list(map(int, input().split()))

cnt = 0
total = 0

for i in arr:
    if i == 0:
        break
    elif i % 2 == 0:
        cnt += 1
        total += i
    else: 
        continue
    
print(cnt, total)