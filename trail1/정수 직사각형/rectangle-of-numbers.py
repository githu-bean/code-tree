N, M = map(int, input().split())

arr_2d = [ [0 for _ in range(M)] for _ in range(N)]

init = 1

for i in range(N):
    for j in range(M):
        arr_2d[i][j] = init
        init += 1

for i in range(N):
    for j in range(M):
        print(arr_2d[i][j], end=' ')
    print()