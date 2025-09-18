T = int(input())

for t in range(1, T + 1):
    N = int(input())
    desired_lights = list(map(int, input().split()))
    lights = [0] * N
    switch_count = 0

    for i in range(N):
        if desired_lights[i] == lights[i]:
            continue

        elif desired_lights[i] == 1:
            for k in range(1, N + 1):
                if (i + 1) * k - 1 < N:
                    if lights[(i + 1) * k - 1] == 0:
                        lights[(i + 1) * k - 1] = 1
                    else:
                        lights[(i + 1) * k - 1] = 0
            switch_count += 1

        elif desired_lights[i] == 0:
            for k in range(1, N + 1):
                if (i + 1) * k - 1 < N:
                    if lights[(i + 1) * k - 1] == 0:
                        lights[(i + 1) * k - 1] = 1
                    else:
                        lights[(i + 1) * k - 1] = 0
            switch_count += 1

    print(f'#{t} {switch_count}')



