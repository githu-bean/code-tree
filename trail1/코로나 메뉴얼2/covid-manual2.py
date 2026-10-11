# 버퍼를 잘 활용하여 입력을 반복문으로 받기
# 주사위 문제처럼 index와 A,B,C,D를 맞추어 풀어보기

arr_count = [0] * 5

for _ in range(3):
    i, j = input().split()
    j = int(j)

    if (i == 'Y') and (j >= 37):
        arr_count[1] += 1
    elif (j >= 37): # 이미 이전 조건에서 37도 이상이고 증상이 있는 경우를 필터링했으므로
        arr_count[2] += 1
    elif (i == 'Y'):
        arr_count[3] += 1
    else:
        arr_count[4] += 1
    
for i in arr_count[1::]:
    print(i, end=' ')

if arr_count[1] >= 2:
    print('E')

# X1 = input().split()
# X2 = input().split()
# X3 = input().split()

# patients = [X1, X2, X3]

# arr = [0] * 4

# for i, (j, k) in enumerate(patients):
#     if (j == "Y") and (int(k) >= 37):
#         arr[0] += 1
#     elif (int(k) >= 37): #and (int(k) >= 37):
#         arr[1] += 1
#     elif (j == "Y"): #and not(int(k) >= 37):
#         arr[2] += 1
#     else:
#         arr[3] += 1
    
# for i in arr:
#     print(i, end=' ')

# if arr[0] >= 2:
#     print('E')