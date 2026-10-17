arr_2d = [ list(map(int, input().split())) for _ in range(4) ]

for arr in arr_2d:
    # print(sum(i))
    total = 0

    for i in arr:
        total += i
    
    print(total)

# comprehension 과정
# arr_2d = []
# for _ in range(4):
#     arr_2d.append(list(map(int, input().split())))