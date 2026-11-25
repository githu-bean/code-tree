n = int(input())

arr = [ input() for _ in range(n) ]

char1 = input()

lst = []

for i in arr:
    if i[0] == char1:
        lst.append(i)

total = 0

for i in lst:
    total += len(i)

print(f"{len(lst)} {total/len(lst):.2f}")