N, M = tuple(map(int, input().split()))

arr_2d_1 = [ list(map(int, input().split())) for _ in range(N)]

arr_2d_2 = [ list(map(int, input().split())) for _ in range(N)]

arr_result = [ [1 for _ in range(M)] for _ in range(N) ]

for i in range(N):
    for j in range(M):
        if arr_2d_1[i][j] == arr_2d_2[i][j]:
            arr_result[i][j] = 0

for i in range(N):
    for j in range(M):
        print(arr_result[i][j], end=' ')
    print()