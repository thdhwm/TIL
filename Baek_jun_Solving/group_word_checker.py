N = int(input())
count_group = 0

for _ in range(N):
    word = list(input())
    black_list = []
    is_group = True

    for i in range(1, len(word)):
        if word[i - 1] != word[i]:
            black_list.append(word[i - 1])

        if i + 1 < len(word) and word[i + 1] in black_list:
            is_group = False
            break

    if is_group:
        count_group += 1

print(count_group)
