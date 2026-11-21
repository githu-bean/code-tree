n = int(input())

arr = [ input() for _ in range(n) ]

count = 0
start_a = 0

for s in arr:
    count += len(s)
    if s[0] == 'a':
        start_a += 1

print(count, start_a)