# append 써서 더 일반적인 코드로 만들기
N = int(input())

arr = [1, N]
index = 2
tmp = 0

while True:
    tmp = arr[index-1] + arr[index-2]
    arr.append(tmp)

    if tmp > 100:
        break

    index += 1

for i in arr:
    print(i, end=' ')

# N = int(input())

# arr = [1, N] + [0] * 98

# for i in range(2, 100):
#     arr[i] = arr[i-2] + arr[i-1]
#     if arr[i] > 100:
#         break

# for i in [j for j in arr if j > 0]:
#     print(i, end=' ')