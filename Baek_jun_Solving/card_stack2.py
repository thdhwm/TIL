from collections import deque
# appendleft
# popleft

N = int(input())
cards = deque([i for i in range(1, N + 1)])

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])
