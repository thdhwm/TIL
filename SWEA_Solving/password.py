for t in range(1, 11):
    length, password = input().split()    # ex. 10, 1238099084
    length = int(length)
    password = list(password)
    stack = []

    for i in range(length):
        if len(stack) > 0 and password[i] == stack[-1]:
            stack.pop()

        else:
            stack.append(password[i])

    print(f'#{t}', (''.join(stack)))
