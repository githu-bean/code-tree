arr = map(int, input().split())

total = 0
cnt = 0

for i in arr:
    if i < 250:
        total += i
        cnt += 1
    else:
        break

print(total, round(total / cnt, 1))