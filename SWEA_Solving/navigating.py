for _ in range(10):
    t, length = map(int, input().split())    # t - testcase 번호, roads - 길의 총 개수
    roads = list(map(int, input().split()))
    nods_1 = [0] * 100
    nods_2 = [0] * 100

    for i in range(length):
        if nods_1[roads[2 * i]] == 0:
            nods_1[2 * i] = roads[2 * i + 1]

        else:
            nods_2[2 * i] = roads[2 * i + 1]

    print(nods_1)
    print(nods_2)

