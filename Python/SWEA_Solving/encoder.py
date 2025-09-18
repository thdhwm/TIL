from collections import deque
import sys
sys.stdin = open('input.txt')

for _ in range(10):
    test_case = int(input())
    password = deque(map(int, input().split()))
    cnt = 1

    while password:
        if cnt == 5:
            if password[0] - cnt > 0:
                password[0] -= cnt
                cnt = 1
                password.append(password.popleft())
            else:
                password[0] = 0
                password.append(password.popleft())
                break

        elif password[0] - cnt > 0:
            password[0] -= cnt
            cnt += 1
            password.append(password.popleft())
        else:
            password[0] = 0
            password.append(password.popleft())
            break

    print(f'#{test_case}', *password)
