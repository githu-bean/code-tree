a, b  = list(map(int, input().split())) # 변수의 수와 리스트 원소의 수가 일치하므로 언패킹

arr = [a, b]

for i in range(2, 10):
    arr.append(arr[i-1] + 2*arr[i-2])

for i in arr:
    print(i, end=' ')