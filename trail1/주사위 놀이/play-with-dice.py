arr = list(map(int, input().split()))

arr_cnt = [0] * 6

for i in arr:
    for j in range(1, 7):
        if i == j:
            arr_cnt[j-1] += 1

for i, value in enumerate(arr_cnt):
    print(f"{i+1} - {value}")