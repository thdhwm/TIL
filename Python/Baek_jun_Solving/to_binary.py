def to_binary(n):
    if n == 1:
        return '1'
    elif n == 0:
        return '0'

    return to_binary(n // 2) + str(n % 2)


N = int(input())

print(to_binary(N))
