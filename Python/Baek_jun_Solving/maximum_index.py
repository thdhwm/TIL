number_list = []
maximum = 0
idx = 0

for _ in range(9):
    number_list.append(int(input()))

for i in range(9):
    if maximum < number_list[i]:
        maximum = number_list[i]
        idx = i + 1

print(maximum)
print(idx)
