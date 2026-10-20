arr_2d = [ list(map(int, input().split())) for _ in range(4)]

tmp = 1
total = 0

for arr in arr_2d:
    for i in arr[0:tmp]:
        total += i
    tmp += 1

print(total)