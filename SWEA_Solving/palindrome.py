for _ in range(10):
    t = int(input())

    table = [[0] for _ in range(100)]
    max_len = 0
    for i in range(100):
        table[i] = list(input().strip())

    for i in range(100):        # 100줄
        for j in range(99):    # 100 글자 모두 에서 1 글자 까지
            for k in range(j + 1):    # 슬라이딩 윈도우
                table_to_compare = table[i][k: 99 - j + k]
                if table_to_compare == table_to_compare[::-1] and len(table_to_compare) > max_len:
                    max_len = len(table_to_compare)

    # .zip???
    print(max_len)


