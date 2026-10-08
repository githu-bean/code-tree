N = int(input())
grades = list(map(float, input().split()))

mean_ = sum(grades) / len(grades)

print(f"{mean_:.1f}")

if mean_ >= 4.0:
    print("Perfect")
elif mean_ >= 3.0:
    print("Good")
else:
    print("Poor")