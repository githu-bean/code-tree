N, Q = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

for i in range(Q):
    query = input().split()

    if query[0] == '1':
        idx = int(query[1]) - 1
        print(arr[idx])

    elif query[0] == '2':
        target = int(query[1])
        idx = 0
        for i, value in enumerate(arr):
            if target == value:
                idx = i + 1
                break
        print(idx)

    else:
        idx1 = int(query[1]) - 1
        idx2 = int(query[2])

        for i in range(idx1, idx2):
            print(arr[i], end=' ')
        print()
