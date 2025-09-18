import sys
sys.stdin = open('input.txt', 'r')

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multi(a, b):
    return a * b


def div(a, b):
    return int(a / b)


def find(depth, numbers, nFuncs):
    global max_val, min_val
    nNum = numbers[:]
    nnFuncs = nFuncs[:]

    if depth == N - 1:
        if min_val > nNum[-1]:
            min_val = nNum[-1]
        if max_val < nNum[-1]:
            max_val = nNum[-1]
        return

    for i in range(4):
        if nnFuncs[i] == 0:
            continue

        temp = nNum[depth + 1]
        nNum[depth + 1] = funcs[i](nNum[depth], nNum[depth + 1])
        nnFuncs[i] -= 1
        find(depth + 1, nNum, nnFuncs)
        nnFuncs[i] += 1
        nNum[depth + 1] = temp


T = int(input())
funcs = [add, sub, multi, div]
for test_case in range(1, T + 1):
    N = int(input())
    nFuncs = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    max_val = -21e8
    min_val = 21e8

    find(0, numbers, nFuncs)

    print(f'#{test_case} {max_val - min_val}')
# ###############################################################################################################
# # problem solving lecture
# import sys
# sys.stdin = open("input.txt")
#
# # 종료조건: 모든 숫자를 고려
# # 시작점: 1개의 숫자부터 시작
# # 누적값: 몇 개 숫자 고려 했는 지, 계산된 결과, 남은 연산자 수
# # 가지의수: 최대 4개(연산자가 없으면 못쓴다)
# def recur(cnt, total, plus, minus, mul, div):
#     global min_result
#     global max_result
#
#     if cnt == N:
#         # 최대, 최소 계산
#         min_result = min(min_result, total)
#         max_result = max(max_result, total)
#         return
#
#     # 덧셈
#     if plus > 0:
#         recur(cnt + 1, total + numbers[cnt], plus - 1, minus, mul, div)
#     # 뺄셈
#     if minus > 0:
#         recur(cnt + 1, total - numbers[cnt], plus, minus - 1, mul, div)
#     # 곱셈
#     if mul > 0:
#         recur(cnt + 1, total * numbers[cnt], plus, minus, mul - 1, div)
#     # 나눗셈
#     if div > 0:
#         recur(cnt + 1, int(total / numbers[cnt]), plus, minus, mul, div - 1)
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     opers = list(map(int, input().split()))
#     numbers = list(map(int, input().split()))
#
#     min_result = 1e9
#     max_result = -1e9
#
#     recur(1, numbers[0], opers[0], opers[1], opers[2], opers[3])
#     print(f'#{tc} {max_result - min_result}')
#
# # print(int(7 / 3))  # 2
# # print(7 // 3)  # 2
# #
# # print(int(-7 / 3))  # -2
# # print(-7 // 3)  # -3
