T = int(input())

for t in range(1, T + 1):
    rods = list(input())
    num_rods = 0
    total = 0

    for i in range(len(rods)):
        if rods[i] == '(':
            num_rods += 1

        else:
            if rods[i - 1] == '(':
                num_rods -= 1
                total += num_rods

            else:
                num_rods -= 1
                total += 1

    print(f'#{t} {total}')

# 22 min.
# pass in 1 go
