arr = list(map(int, input().split()))

cnt = 0
total = 0

for i in arr:
    if i == 0:
        break
    else:
        cnt += 1
        total += i

print(f"{total} {total/cnt:.1f}")