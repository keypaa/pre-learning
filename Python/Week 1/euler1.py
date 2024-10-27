both = []


for i in range(999, -1, -1):
    if i % 3 == 0 or i % 5 == 0:
        print(i,"can be divided by 3")
        both.append(i)
print(both)

total = sum(both)
print(total)

total = sum(i for i in range(999, 0, -1) if i % 3 == 0 or i % 5 == 0)
print(total)