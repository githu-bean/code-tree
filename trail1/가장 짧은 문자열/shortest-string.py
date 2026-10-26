str1 = input()
str2 = input()
str3 = input()

len1 = len(str1)
len2 = len(str2)
len3 = len(str3)

lst = []

lst.append(len1)
lst.append(len2)
lst.append(len3)

max = 0
min = 21

for i in lst:
    if i > max:
        max = i
    if i < min:
        min = i
    
print(max - min)