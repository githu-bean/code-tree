arr = list(map(int, input().split()))

cnt = 0

for i in arr:
    if i == 0:
        break

    else:
        cnt += 1

print(sum(arr[cnt-1::-1][:3]))
# 1. 0을 포함하는 배열이 주어졌을 때 0의 위치를 cnt에 저장
# 2. 0의 위치 바로 앞까지 원소를 순서를 바꾸어 정렬
# 3. 2의 배열의 0,1,2 인덱스 원소를 반환, 즉 0이 주어졌을 때 0의 위치에서 앞 세 개의 원소를 반환
# 4. sum