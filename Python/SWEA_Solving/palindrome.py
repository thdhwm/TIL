for _ in range(10):
    t = int(input().strip())
    table = [list(input().strip()) for _ in range(100)]
    max_len = 1

    # 행 검사
    for length in range(100, 0, -1):  # 100 부터 1까지
        found = False
        for i in range(100):
            for start in range(101 - length):
                is_palindrome = 1  # 회문인지 검사 시작
                table_to_compare = table[i][start:start + length]
                for l in range(length // 2):
                    if table_to_compare[l] != table_to_compare[-l - 1]:
                        is_palindrome = 0    # 회문 아니면 break
                        break
                if is_palindrome:      # 회문이면 max_len 저장하고 행 검사 종료
                    max_len = length
                    found = True
                    break
            if found:
                break
        if found:
            break

    # 열 검사 (100부터 max_len 까지만, 더 작아지면 필요 없음)
    column = list(zip(*table))    # 행열 뒤집기
    for length in range(100, max_len, -1):
        found = False
        for i in range(100):
            for start in range(101 - length):
                is_palindrome = 1  # 회문인지 검사 시작
                table_to_compare = column[i][start:start + length]
                for l in range(length // 2):
                    if table_to_compare[l] != table_to_compare[-l - 1]:
                        is_palindrome = 0    # 회문 아니면 break
                        break
                if is_palindrome:      # 회문이면 max_len 저장하고 행 검사 종료
                    max_len = length
                    found = True
                    break
            if found:
                break
        if found:
            break

    print(f'#{t} {max_len}')







# def is_palindrome(txt):
#     for idx in range(len(txt)//2):
#         if txt[idx] != txt[- 1 - idx]:
#             return False
#     return True
#
#
# for _ in range(10):
#     t = int(input().strip())
#
#     table = [[0] for _ in range(100)]
#     max_len_row = 0
#     max_len_column = 0
#
#     for i in range(100):
#         table[i] = list(input().strip())
#
# # 행 검사
#     for i in range(100):        # 100줄
#         for j in range(99, -1, -1):    # 100 글자 모두 에서 1 글자 까지
#             for k in range(99 - j + 1):    # 슬라이딩 윈도우
#                 table_to_compare = table[i][k: j + k + 1]
#
#                 if is_palindrome(table_to_compare):
#                     max_len_row = len(table_to_compare)
#                     break
#
#             if is_palindrome(table_to_compare):
#                 break
#
#         if is_palindrome(table_to_compare):         # 젤 긴거 찾았으니 나머지 볼 필요 X
#             break
#
#
# # 열 검사
#     column = list(zip(*table))
#     for i in range(100):        # 100줄
#         for j in range(99, -1, -1):    # 100 글자 모두 에서 1 글자 까지
#             for k in range(99 - j + 1):    # 슬라이딩 윈도우
#                 table_to_compare = column[i][k: j + k + 1]
#
#                 if is_palindrome(table_to_compare):
#                     max_len_column = len(table_to_compare)
#                     break
#
#             if is_palindrome(table_to_compare):
#                 break
#
#         if is_palindrome(table_to_compare):            # 젤 긴거 찾았으니 나머지 볼 필요 X
#             break
#
#     print(f'#{t} {max_len_column}')

