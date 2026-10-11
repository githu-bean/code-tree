N = int(input())

cnt = 0
i = 1
tmp = 0

while cnt <= 1:
    tmp = N*i
    print(tmp, end=' ')
    if tmp % 5 == 0:
        cnt += 1
    i += 1