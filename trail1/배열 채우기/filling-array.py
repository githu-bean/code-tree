arr = map(int, input().split())
arr_new = []

for i in arr:
    if i == 0:
        break
    else:
        arr_new.append(i)

for i in range(-1, -len(arr_new)-1, -1):
    print(arr_new[i], end=' ')
