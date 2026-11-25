arr = [ input() for _ in range(10) ]

char1 = input()

lst = []

for i in arr:
    if i[-1] == char1:
        lst.append(i)

if len(lst) == 0:
    print(None)
else:
    for i in lst:
        print(i)