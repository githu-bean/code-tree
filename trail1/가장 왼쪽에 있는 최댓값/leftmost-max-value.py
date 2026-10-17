n = int(input())
arr = list(map(int, input().split()))

idx_list = []

while True:
    idx_max = 0

    for i in range(n):
        if arr[idx_max] < arr[i]:
            idx_max = i

    idx_list.append(idx_max)

    n = idx_max

    if idx_max == 0:
        break

for i in idx_list:
    print(i+1, end=' ')




# n = int(input())
# arr = list(map(int, input().split()))

# # Please write your code here.
# max_idxs = [0] * 1000

# cnt = 0 # 몇 번째 최댓값을 찾고 있는지

# while True:

#     for idx, value in enumerate(arr):
#         if arr[max_idxs[cnt]] < value: # cnt 번째 최댓값 인덱스를 가져와서 arr 인덱싱, 현재 값보다 작으면 =
#             max_idxs[cnt] = idx # 그 값이 있는 인덱스를 최댓값 인덱스로 교체
#             # print(idx)

#     if max_idxs[cnt] == 0:
#         max_idxs = max_idxs[:cnt+1]
#         break

#     arr = arr[0:max_idxs[cnt]]
#     #print(arr)
#     cnt += 1

# for i in max_idxs:
#     print(i+1, end=' ')