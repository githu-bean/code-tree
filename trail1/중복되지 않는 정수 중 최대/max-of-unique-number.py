# 최댓값을 찾고 -> 중복이 없는 경우만 출력
N = int(input())

arr = list(map(int, input().split()))

max = -1

for i in arr:

    if max < i:
        cnt = 0

        for j in arr:

            if i == j:
                cnt += 1
        if cnt == 1:
            max = i

print(max)

    


# # 중복없는 리스트 -> 최댓값 찾기 순서
# N = int(input())

# arr = list(map(int, input().split()))

# unique_lst = []

# for i in range(N):
#     cnt = 0

#     for j in range(N):
#         if i != j and arr[i] == arr[j]:
#             cnt += 1

#     if cnt == 0:
#         unique_lst.append(arr[i])

# # print(unique_lst)

# if len(unique_lst) >= 1:            
#     max = unique_lst[0]
#     for i in unique_lst:
#         if max < i:
#             max = i
#     print(max)
# else:
#     print(-1)