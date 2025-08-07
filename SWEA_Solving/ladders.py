for _ in range(10):
    t = int(input())
    table = [[0] * 100 for _ in range(100)]
    maximum = -21e8

    for i in range(100):
        table[i] = list(map(int, input().split()))

    for row in table:
        if maximum < sum(row):
            maximum = sum(row)

    for j in range(100):
        column_max = 0
        for i in range(100):
            column_max += table[i][j]
        if maximum < column_max:
            maximum = column_max

    diagonal_max = 0
    rev_diagonal_max = 0
    for i in range(100):
        diagonal_max += table[i][i]
        rev_diagonal_max += table[99 - i][i]

    if maximum < diagonal_max:
        maximum = diagonal_max
    elif maximum < rev_diagonal_max:
        maximum = rev_diagonal_max

    print(f'#{t} {maximum}')

