from collections import deque

N, K = map(int, input().split())        # ex. 7 3
circle = deque([x for x in range(1, N + 1)])    # ex. [1, 2, 3, 4, 5, 6, 7]
josephus = []

while circle:
    for _ in range(K - 1):          # K -1번 뒤로 보내고
        circle.append(circle.popleft())
    josephus.append(circle.popleft())    # K 번째 josephus에 더하기

josephus.extend(circle)      # 남은거 더해주기
result = str(josephus)[1: -1]     # 출력 형식 맞추기
print(f'<{result}>')
