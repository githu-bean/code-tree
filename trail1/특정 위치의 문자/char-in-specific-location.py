word = ['L', 'E', 'B', 'R', 'O', 'S']

ch = input()

idx = -1

for i, char in enumerate(word):
    if word[i] == ch:
        idx = i

if idx == -1:
    print("None")
else:
    print(idx)