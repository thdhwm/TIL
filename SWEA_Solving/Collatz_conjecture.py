T = int(input())

for t in range(1, T + 1):
    Collatz = int(input())
    count_collatz = 0

    while Collatz != 1:
        if Collatz % 2 == 0:
            Collatz //= 2
            count_collatz += 1

        else:
            Collatz = 3 * Collatz + 1
            count_collatz += 1

    print(f'#{t} {count_collatz}')

# ######################## 위에는 생각난 대로 아래는 재귀로 ########################### #
#
# T = int(input())
#
#
# def Collatz_conjecture(Collatz):
#     global count_collatz
#     if Collatz == 1:
#         return
#
#     if Collatz % 2 == 0:
#         Collatz //= 2
#         count_collatz += 1
#         return Collatz_conjecture(Collatz)
#
#     else:
#         Collatz = 3 * Collatz + 1
#         count_collatz += 1
#         return Collatz_conjecture(Collatz)
#
#
# for t in range(1, T + 1):
#     Collatz = int(input())
#     count_collatz = 0
#
#     Collatz_conjecture(Collatz)
#
#     print(f'#{t} {count_collatz}')
