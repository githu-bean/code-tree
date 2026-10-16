N = int(input())

arr = list(map(int, input().split()))

unique_lst = []

for i in range(N):
    cnt = 0

    for j in range(N):
        if i != j and arr[i] == arr[j]:
            cnt += 1

    if cnt == 0:
        unique_lst.append(arr[i])

# print(unique_lst)

if len(unique_lst) >= 1:            
    max = unique_lst[0]
    for i in unique_lst:
        if max < i:
            max = i
    print(max)
else:
    print(-1)








# n = int(input())
# nums = list(map(int, input().split()))

# # Please write your code here.
# cnt_list = [0] * 1001

# cnt = 0

# for i in nums:
#     cnt = 0
#     for j in nums:
#         if i == j:
#             cnt += 1
    
#     cnt_list[i] = cnt

# #print(cnt_list)

# dup_list = []

# for i in range(1001):
#     if cnt_list[i] == 1:
#         dup_list.append(i)
    
    
# print(max(dup_list) if len(dup_list) >= 1 else -1)
