def fibo(n):
    if n == 0:
        return 0

    elif n < 3:
        return 1

    return fibo(n - 1) + fibo(n - 2)


N = int(input())

print(fibo(N))
