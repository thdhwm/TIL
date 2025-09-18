for _ in range(10):
    t = int(input())
    table = [[0] * 100 for _ in range(100)]

    for i in range(100):
        table[i] = list(map(int, input().split()))

####################### 사다리 생성 끝 ############################

    start_x = 0
    start_y = 99
# 출발점 찾기
    for i in range(100):
        if table[99][i] == 2:
            start_x = i             # 출발점 x 좌표

    while start_y > 0:
        if 0 <= start_x - 1:
            if table[start_y][start_x - 1] == 1:    # 좌측 사다리
                start_x -= 1
                while table[start_y + 1][start_x] == 0:
                    start_x -= 1
                start_y -= 1
                continue    # 사다리 끝나고 밑에 if 바로하면 안되니까

        if start_x + 1 <= 99:
            if table[start_y][start_x + 1] == 1:    # 우측 사다리
                start_x += 1
                while table[start_y + 1][start_x] == 0:
                    start_x += 1

        start_y -= 1                              # 없으면 올라가

    print(f'#{t} {start_x}')

    # 밑에 if를 elif 하면 되는거였자나? ㅃㅇㅇ
