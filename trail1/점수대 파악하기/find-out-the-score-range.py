arr = list(map(int, input().split()))

arr_cnt = [0] * 10

for i in arr:
    if i == 0:
        break
    elif i < 10:
        continue
    else:
        arr_cnt[i//10 - 1] += 1

# 더 쉽게
for i in range(9, -1, -1):
    print(f"{i*10 + 10} - {arr_cnt[i]}")

# for i,v in enumerate(arr_cnt[9::-1]):
#     print(f"{110 -  (i+1) * 10} - {v}")