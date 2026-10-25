str1, str2 = input().split()

n = len(str1); m = len(str2)

if n > m:
    print(str1, n)
elif n < m:
    print(str2, m)
else:
    print('same')