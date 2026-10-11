arr = list(map(int, input().split()))

arr_cnt = [0] * 9

for i in arr:
    if i == 0:
        break

    if i > 10:
        arr_cnt[i//10 - 1] += 1
    else:
        continue

for i,v in enumerate(arr_cnt):
    print(f"{i+1} - {v}")