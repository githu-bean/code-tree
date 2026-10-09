arr = list(map(int, input().split()))

for index, value in enumerate(arr):
    if value % 3 == 0:
        print(arr[index - 1])
        break


# arr = list(map(int, input().split()))

# cnt = 0

# for i in arr:
#     if i % 3 != 0:
#         cnt += 1
#     else:
#         break

# print( arr[cnt-1] )