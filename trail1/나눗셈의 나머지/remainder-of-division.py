a, b = tuple(map(int, input().split()))

count = [0] * 1000

while a > 0 and b >= 2:
    #print(a, a%b)
    count[a % b] += 1
    a = a // b

    if a == 1:
        break
    

print(sum([i**2 for i in count]))