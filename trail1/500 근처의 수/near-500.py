arr = list(map(int, input().split()))

maxUnder500 = 0

for i in arr:
    if maxUnder500 < i and i < 500:
        maxUnder500 = i

minOver500 = 1000

for i in arr:
    if minOver500 > i and i > 500:
        minOver500 = i

print(maxUnder500, minOver500)