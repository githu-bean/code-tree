word = input()

word_lst = ["apple", "banana", "grape", "blueberry", "orange"]

result = []

for w in word_lst:
    if w[2] == word or w[3] == word:
        result.append(w)

for w in result:
    print(w)

print(len(result))