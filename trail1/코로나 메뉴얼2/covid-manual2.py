X1 = input().split()
X2 = input().split()
X3 = input().split()

patients = [X1, X2, X3]

arr = [0] * 4

for i, (j, k) in enumerate(patients):
    if (j == "Y") and (int(k) >= 37):
        arr[0] += 1
    elif (j == "N") and (int(k) >= 37):
        arr[1] += 1
    elif (j == "Y") and not(int(k) >= 37):
        arr[2] += 1
    else:
        arr[3] += 1
    
for i in arr:
    print(i, end=' ')

if arr[0] >= 2:
    print('E')