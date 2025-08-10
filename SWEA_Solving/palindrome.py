for _ in range(10):
    t = int(input().strip())
    
    table = [[0] for _ in range(100)]
    max_len = 0
    for i in range(100):
        table[i] = list(input().strip())

# 행 검사
    for i in range(100):        # 100줄
        for j in range(99):    # 100 글자 모두 에서 1 글자 까지
            for k in range(j + 1):    # 슬라이딩 윈도우
                table_to_compare = table[i][k: 99 - j + k]
                is_palindrome = 1

                for l in range(len(table_to_compare) // 2):        # 회문인지 검사
                    if table_to_compare[l] != table_to_compare[-l - 1]:
                        is_palindrome = 0
                        break

                if is_palindrome == 1:
                    max_len = len(table_to_compare)
                    break

            if is_palindrome == 1:          
                break

        if is_palindrome == 1:            # 젤 긴거 찾았으니 나머지 볼 필요 X
            break


# 열 검사
    column = list(zip(*table))
    for i in range(100):        # 100줄
        for j in range(99):    # 100 글자 모두 에서 1 글자 까지
            for k in range(j + 1):    # 슬라이딩 윈도우
                table_to_compare = column[i][k: 99 - j + k]
                is_palindrome == 1

                for l in range(len(table_to_compare) // 2):        # 회문인지 검사

                    if table_to_compare[l] != table_to_compare[-l - 1]:
                        is_palindrome = 0
                        break

                if is_palindrome == 1 and max_len < len(table_to_compare):
                    max_len = len(table_to_compare)
                    break

            if is_palindrome == 1:          
                break

        if is_palindrome == 1:            # 젤 긴거 찾았으니 나머지 볼 필요 X
            break


    print(f'#{t} {max_len}')


# for _ in range(10):
#     t = int(input().strip())
#     table = [list(input().strip()) for _ in range(100)]
#     max_len = 1

#     # 행 검사 (길이 큰 것부터 검사)
#     for length in range(100, 0, -1):  # 100 ~ 1
#         found = False
#         for i in range(100):
#             for start in range(101 - length):
#                 is_palindrome = 1  # 여기서 매번 초기화
#                 seq = table[i][start:start + length]
#                 for l in range(length // 2):
#                     if seq[l] != seq[-l - 1]:
#                         is_palindrome = 0
#                         break
#                 if is_palindrome:
#                     max_len = length
#                     found = True
#                     break
#             if found:
#                 break
#         if found:
#             break

#     # 열 검사 (길이 큰 것부터 검사, max_len보다 작아지면 중단)
#     for length in range(100, max_len, -1):
#         found = False
#         for col in range(100):
#             for start in range(101 - length):
#                 is_palindrome = 1  # 여기서 매번 초기화
#                 seq = [table[start + k][col] for k in range(length)]
#                 for l in range(length // 2):
#                     if seq[l] != seq[-l - 1]:
#                         is_palindrome = 0
#                         break
#                 if is_palindrome:
#                     max_len = length
#                     found = True
#                     break
#             if found:
#                 break
#         if found:
#             break

#     print(f'#{t} {max_len}')