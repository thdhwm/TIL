# T = int(input()) #태스트 케이스 수

# for t in range(1, T + 1):
#     day = int(input())
#     prices = list(map(int, input().split()))
#     print(max(prices))







# T = int(input())
# for test_case in range(1, T+1) :
# day = int(input())                             ## day = 1
# prices = list(map(int, input().split()))       ##  [3, 5, 9]  가정

# max_prices = [0]*day                           ## max_prices 라는 배열 만듬 [0, 0, 0]
# max_price = prices[-1]                         ## max_price 를 prices 배열 마지막 원소로 지정 9
# for i in range(day-1, -1, -1) :                # range -> 0, -1, -1 
# max_price = max(max_price, prices[i])          # prices -> 
# max_prices[i] = max_price

# benefit = 0
# for i in range(day) :
# if max_prices[i] - prices[i] > 0 :
# benefit += (max_prices[i] - prices[i])

######################################################################################

T = int(input())

for t in range(1, T + 1):
    N = int(input())

    