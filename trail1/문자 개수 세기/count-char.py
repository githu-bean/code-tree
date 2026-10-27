string = input()
find = input()

cnt = 0

for st in string:
    if st == find:
        cnt += 1

print(cnt)