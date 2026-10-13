a, b = tuple(map(int, input().split()))

count = [0] * 1000

while a > 1:
    count[a % b] += 1
    a = a // b

print(sum([i**2 for i in count]))