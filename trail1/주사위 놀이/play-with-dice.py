# 더 쉬운 코드
# index 0을 버리고 들어온 숫자 자체를 인덱스로 사용하는 방법
# 주사위가 아니라 다른 숫자 범위가 들어오는 경우 일반적인 코드로는 사용하기 어려움
arr = list(map(int, input().split()))

arr_cnt = [0] * 7

for i in arr: # 3이 들어오면 index 3에 카운팅, 주사위 눈금 중 0은 없으므로 index 0은 사용되지 않음
    arr_cnt[i] += 1

for i in range(1, 7):
    print(f"{i} - {arr_cnt[i]}")


# arr = list(map(int, input().split()))

# arr_cnt = [0] * 6

# for i in arr:
#     for j in range(1, 7):
#         if i == j:
#             arr_cnt[j-1] += 1

# for i, value in enumerate(arr_cnt):
#     print(f"{i+1} - {value}")