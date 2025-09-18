import sys
sys.stdin = open('input.txt')

#
# def three_month(arr):    # 슬라이딩 윈도우 최대인 구간 3 개월권으로
#     global total
#     max_window = max(arr)
#     # print(arr)
#     if max_window > monthly_3:
#         for i in range(len(arr)):
#             if arr[i] == max_window:
#                 extended_plan[i:i+3] = [0, 0, 0]
#                 total += monthly_3
#
#                 result_list = sliding(extended_plan)
#
#                 three_month(result_list)
#                 return
#     else:
#         return
#
# def sliding(arr):
#     sliding_window = [0] * 16    # 12month, +2 front and back
#     initial = sum(arr[:3])
#     sliding_window[0] = initial
#     for k in range(1, 14):
#         initial -= arr[k - 1]
#         initial += arr[k + 2]
#         sliding_window[k] = initial
#
#     return sliding_window
#
#
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     daily, monthly, monthly_3, annually = map(int, input().split())
#     monthly_plan = list(map(int, input().split()))
#     total = 0
#
#     for i in range(len(monthly_plan)):
#         if monthly > daily * monthly_plan[i]:
#             monthly_plan[i] = daily * monthly_plan[i]
#         else:
#             monthly_plan[i] = monthly
#     print(monthly_plan)
    # extended_plan = [0, 0] + monthly_plan + [0, 0]
    # # print(extended_plan)
    # result = sliding(extended_plan)
    # # print(result)
    # three_month(result)
    # # print(total, extended_plan)
    # total += sum(extended_plan)
    #
    # print(f'#{test_case}', total if total < annually else annually)

# ##################################################################
# sliding 해서 max 인거는 안댐 greedy 적으로 안된다..!!!
# 다른 방법....
T = int(input())

for test_case in range(1, T + 1):
    daily, monthly, monthly_3, annually = map(int, input().split())
    plan = list(map(int, input().split()))

    monthly_plan = [0] * 12
    for i in range(len(monthly_plan)):    # 달마다 1일권 vs 1달권 비교
        if monthly > daily * plan[i]:
            monthly_plan[i] = daily * plan[i]
        else:
            monthly_plan[i] = monthly

    dp = [0] * 12               # 12개월
    dp[0] = monthly_plan[0]     # 처음 dp 초기화

    for i in range(1, 12):
        dp[i] = dp[i-1] + monthly_plan[i]  # 다음달 = 이전에 있던 달 비용 + 이번달

        if i >= 3:     # 3달권 사용가능 할 때부터, 적용한거 vs 안한거 비교
            dp[i] = min(dp[i], dp[i-3] + monthly_3)

        elif i == 2:     # 2달까지는 하드 코딩
            dp[i] = min(dp[i], monthly_3)

    total = dp[11]      # 3달권까지 다본 total
    print(f'#{test_case}', total if total < annually else annually)


# ######################################################################################
# 문제풀이 강의
# 방법 2가지...
# 1. 다 보기!
# 1월에 1일권 쓰는거, 1달권 사는거, 3달권 사는거(이러면 2,3월 패스)... 12월에 .. 구하고 합이 최소인거

# 2. dp
