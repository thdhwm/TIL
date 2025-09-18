import sys
sys.stdin = open('input.txt', 'r')
T = int(input())


def combination(arr, n):       # from arr, pick n elements
    result = []            # ex. arr - [0, 1, 2, 3], n - 2
    # if n > len(arr):
    #     return result

    if n == 1:
        for i in arr:
            result.append([i])

    elif n > 1:
        for i in range(len(arr) - n + 1):    # i - 0, 1, 2
            for j in combination(arr[i + 1:], n - 1): # pick 1, comb rest of the elements
                result.append([arr[i]] + j)

    return result


def diff(first, second):     # get difference between two dishes
    first_comb = combination(first, 2)      # synergy pairs in first dish
    second_comb = combination(second, 2)    # synergy pairs in second dish
    first_total = 0
    second_total = 0

    for i, j in first_comb:             # total of synergies in first dish
        first_total += graph[i][j] + graph[j][i]

    for i, j in second_comb:            # total of synergies in second dish
        second_total += graph[i][j] + graph[j][i]

    difference = abs(first_total - second_total)

    return difference


for test_case in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    synergy = combination([i for i in range(N)], N//2)
    # pick half of the elements in range N, other half is automatically decided
    min_diff = 21e8
    for i in range(len(synergy)//2):
        ans = diff(synergy[i], synergy[-(i + 1)])
        min_diff = min(min_diff, ans)

    print(f'#{test_case} {min_diff}')

# ##################################################################################################
# # problem solving lecture
# # N // 2 개를 A에 넣고, 나머지는 B라고 가정
# # -> 모든 재료를 골라보면서, A에 넣자
# # -> visited 로 구현 (1이라면 A에 들어감, 0이라면 B에 들어감)
#
# def cal_synergy(li):
#     total = 0
#
#     for i in range(len(li)):
#         for j in range(i + 1, len(li)):
#             total += arr[li[i]][li[j]] + arr[li[j]][li[i]]
#
#     return total
#
#
# def get_synergy():
#     A_list, B_list = [], []
#     for i in range(N):
#         if visited[i]:
#             A_list.append(i)
#         else:
#             B_list.append(i)
#
#     return cal_synergy(A_list), cal_synergy(B_list)
#
# # 종료조건: 재료의 반을 선택 --> 시너지 계산
# # 가지의수: 모든 재료(N)
# def recur(cnt, prev):
#     global min_answer
#     if cnt == N // 2:
#         # 시너지 계산
#         a_total, b_total = get_synergy()
#         min_answer = min(min_answer, abs(a_total - b_total))
#         return
#
#     for food_number in range(prev + 1, N):
#         if visited[food_number]:  # 이미 쓴 재료는 안쓴다.
#             continue
#
#         visited[food_number] = 1
#         recur(cnt + 1, food_number)
#         visited[food_number] = 0
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     visited = [0] * N
#     min_answer = 21e8
#     recur(0, 0)
#     print(f'#{tc} {min_answer}')