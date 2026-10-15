n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
cnt_list = [0] * 1001

cnt = 0

for i in nums:
    cnt = 0
    for j in nums:
        if i == j:
            cnt += 1
    
    cnt_list[i] = cnt

#print(cnt_list)

dup_list = []

for i in range(1001):
    if cnt_list[i] == 1:
        dup_list.append(i)
    
    
print(max(dup_list) if len(dup_list) >= 1 else -1)
