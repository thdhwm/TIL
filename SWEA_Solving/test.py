T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))
    card_list = [0] * 10

    greatest = 0
    for i in arr:
        card_list[i] += 1
        if card_list[i] >= greatest:
            greatest = card_list[i]

    for i in range(9, -1, -1):
        if card_list[i] == greatest:
            greatest_num = i
            break

    print(f'#{t} {greatest_num} {greatest}')





