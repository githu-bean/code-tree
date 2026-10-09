N = int(input())

arr = [0] * N

for i in range(N):
    arr[i] = tuple(map(int, input().split()))

cnt = 0

PnF = [0] * N

for i, score in enumerate(arr):
    if sum(score) / len(score) >= 60:
        cnt += 1
        PnF[i] = "pass"
    else:
        PnF[i] = "fail"

for i in PnF:
    print(i)

print(cnt)