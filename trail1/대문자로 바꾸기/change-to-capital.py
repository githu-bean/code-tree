arr_2d = [ list(input().split()) for _ in range(5) ]

for arr in arr_2d:
    for j in arr:
        print(j.upper(), end=' ')
    print()
    