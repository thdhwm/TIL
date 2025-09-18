T = int(input())

for t in range(1, T + 1):
    x1, y1, x2, y2 = map(int, input().split())  # View 1
    a1, b1, a2, b2 = map(int, input().split())  # View 2

    case = 0

    overlap_x = min(x2, a2) - max(x1, a1)
    overlap_y = min(y2, b2) - max(y1, b1)

    if overlap_x > 0 and overlap_y > 0:
        case = 1

    elif (overlap_x == 0 and overlap_y > 0) or (overlap_y == 0 and overlap_x > 0):
        case = 2

    elif overlap_x == 0 and overlap_y == 0:
        case = 3

    else:
        case = 4

    print(f'#{t} {case}')