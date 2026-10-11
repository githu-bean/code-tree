# 배열을 이용하여 해결
N = int(input())
arr = [0] * 10
cnt = 0

for i in range(10):
    arr[i] = N*(i+1)

for i in arr:
    print(i, end=' ')
    if i % 5 == 0:
        cnt += 1
    if cnt >= 2:
        break
    i += 1

# N = int(input())

# cnt = 0
# i = 1
# tmp = 0

# while cnt <= 1:
#     tmp = N*i
#     print(tmp, end=' ')
#     if tmp % 5 == 0:
#         cnt += 1
#     i += 1