n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
answer = 0

for i in range(n):
    for j in range(i, n):
        if price[i] < price[j]:
            if answer < price[j] - price[i]:
                answer = price[j] - price[i]

print(answer)