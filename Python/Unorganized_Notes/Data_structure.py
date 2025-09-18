# DAT (Direct Address Table)
# [1, 3, 2, 3, 2, 5, 7]
# 0~9 사이의 숫자가 여러 개 저장되어 있다
# 각 숫자가 몇 번씩 나왔는 지 출력하라

# 데이터가 추가, 변경 되면?
# 여러 번 호출하는 문제면?

# python
# -> 딕셔너리로 쉽게 해결

# 파이썬 아니면 어캄?
# - 리스트 인덱스를 key처럼 활용



####################딕셔너리####################
                            ################ 내가 한거 ############### 걍 오답,,,,,

# for t in range(1, T + 1):

#     H, W = map(int, input().split())
    
#     table = [list(map(int, input().split())) for _ in range(H)]

#     employee_of_the_month = {}
#     for i in range(H):
#         for j in range(W):
#             employee_of_the_month[table[i][j]] = 0
    
#     for i in range(H):
#         for j in range(W):
#             employee_of_the_month[table[i][j]] += 1

#     greatest = 0
#     greatest_list = []
#     for value in employee_of_the_month:

#         if employee_of_the_month[value] >= greatest:
#             greatest = value
    
#     for value in employee_of_the_month:
#         if employee_of_the_month[value] == employee_of_the_month[greatest]:
#             greatest_list.append(value)

#     print(f'#{t} {min(greatest_list)}')


####################################################################################
############################ 강의 들은거 list, index 사용 ############################
T = int(input())

for t in range(1, T + 1):
    H, W = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(H)]      # 입력 다 받음

    data = [0] * 10000001    # 입력 범위 1 <= 사원번호 <= 10,000,000 이고 인덱스를 사용할꺼라서
    
    max_count = 0
    max_index = 0

    for i in range(H):
        for j in range(W):
            number = table[i][j]
            data[number] += 1              # 사원번호 나올떄마다 카운트 +1

            if max_count < data[number]:
                max_count = data[number]         # 카운트가 가장 많은 사원 번호 카운트 수

    # max_count 가 2개 이상일 때,
    # max_index 는 한 번에 구할 수 없으니
    # 아래처럼 한 번 더 반복시켜 주어야 한다.

    for i in range(10000001):
        if data[i] == max_count:
            max_index = i                # 가장 처음 나오는 max -> 가장 작은 사원 번호
            break

    print(f'#{t} {max_index}')

####################################################################################
############################### 딕셔너리? 어캄? 해봐?? ################################
# T = int(input())

# for t in range(1, T + 1):
#     H, W = map(int, input().split())
#     table = [list(map(int, input().split())) for _ in range(H)]

# for i in range(H):
#     for j in range(W):         # 사원 번호 딕셔너리로 저장?
        

