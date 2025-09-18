

for t in range(10):
    dumps = int(input())
    table = list(map(int, input().split()))
    box_heights = [0] * 101
    high = 0
    low = 101

    for box in table:
        box_heights[box] += 1

    for _ in range(dumps):
        for i in range(101):
            if box_heights[i] != 0:
                box_heights[i] -= 1
                box_heights[i + 1] += 1
                if box_heights[i] == 0:
                    low = i + 1
                else:
                    low = i
                break

        for i in range(100, -1, -1):
            if box_heights[i] != 0:
                box_heights[i] -= 1
                box_heights[i - 1] += 1
                if box_heights[i] == 0:
                    high = i - 1
                else:
                    high = i
                break

    print(f'#{t + 1} {high - low}')
