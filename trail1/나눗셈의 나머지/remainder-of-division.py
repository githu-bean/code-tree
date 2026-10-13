a, b = tuple(map(int, input().split()))

count = [0] * 10 # 문제에서 B <= 10 이므로 나머지는 0부터 10까지 나올 수 있음

while a > 1:
    count[a % b] += 1
    a = a // b

print(sum([i**2 for i in count]))