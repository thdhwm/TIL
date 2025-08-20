import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    N, M, K = map(int, input().split()) # N 문제, M 개 맞춤, K개 연속 정답시 2배
    total = 0
    incorrect = N - M
    cnt_correct = 0
    cnt_incorrect = 0
    in_success = 0
    if M < K or incorrect * K >= N:
        total = M

    elif M == K:
        total = M * 2

    else:
        remainders = N - incorrect * K
        while remainders >= K:
            total = (total + K) * 2
            remainders -= K

        total += remainders + (incorrect * (K - 1))

    print(f'#{t} {total}')


# 겠냐고 겠냐고 되겠냐고 으엉엉엉ㅇ엉엉엉ㅇㅇ으
# def correct(prev):
#     global total, in_success, cnt_correct, min_total
#     if cnt_correct == M and cnt_incorrect == N - M:
#         if min_total > total:
#             min_total = total
#         return min_total
#
#     if cnt_correct == M:
#         incorrect('c')
#
#     cnt_correct += 1
#     total += 1
#     if prev == 'c':
#         in_success += 1
#     if in_success == K:
#         total *= 2
#
#     correct('c')
#     incorrect('c')
#
#
# def incorrect(prev):
#     global total, in_success, cnt_incorrect, min_total
#     if cnt_correct == M and cnt_incorrect == incorrect:
#         if min_total > total:
#             min_total = total
#         return min_total
#
#     if cnt_incorrect == N - M:
#         correct('i')
#
#     cnt_incorrect += 1
#     in_success = 0
#
#     correct('i')
#     incorrect('i')
#
#
# N, M, K = map(int, input().split()) # N 문제, M 개 맞춤, K개 연속 정답시 2배
# total = 0
# incorrect = N - M
# cnt_correct = 0
# cnt_incorrect = 0
# in_success = 0
# min_total = 21e8
#
# print(correct('n'))
