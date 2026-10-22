arr_2d_1 = [ list(map(int, input().split())) for _ in range(3) ]
input()
arr_2d_2 = [ list(map(int, input().split())) for _ in range(3) ]

arr_result = [ [0 for _ in range(3)] for _ in range(3) ]

for i in range(3):
    for j in range(3):
        arr_result[i][j] = arr_2d_1[i][j] * arr_2d_2[i][j]

for i in range(3):
    for j in range(3):
        print(arr_result[i][j], end=' ')
    print()