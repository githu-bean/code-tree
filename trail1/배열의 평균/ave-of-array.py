arr_2d = [ list(map(int, input().split())) for _ in range(2) ]

# comprehension을 다시 상기시키자.
# 1. arr_2d = []
# 2. for _ in range(2)
# 3. arr = list(map(int, input().split()))
# 4. arr_2d.append(arr)
tmp = []

for arr in arr_2d:
    print(f"{sum(arr) / len(arr):.1f}", end=' ')
    tmp.append(sum(arr) / len(arr))

col_sum = [0] * 4
for arr in arr_2d:
    for i, v in enumerate(arr):
        col_sum[i] += v

print()
for i in col_sum:
    print(f"{i / 2:.1f}", end=' ')

print()
print(f"{sum(tmp)/2:.1f}")