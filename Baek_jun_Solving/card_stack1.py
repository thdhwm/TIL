# N = int(input())
# cards = []
# result = []
#
# for i in range(1, N + 1):
#     cards.append(i)
#
# while len(cards) > 1:
#     trash = cards.pop(0)
#     result.append(trash)
#
#     cards.append(cards[0])
#     cards.pop(0)
#
# print(*result, cards[0])


###################### 위에 내 코드, 아래 강사님 코드 ######################################################


N = int(input())

cards = [i for i in range(N, 0, -1)]

# list.insert(index, value)  -> value 를 list 의 index 에 삽입

while len(cards) > 1:
    print(cards.pop(), end=' ')  # 제일 뒤에 걸 뽑아서 출력
    cards.insert(0, cards.pop())  # 제일 뒤를 뽑아서, 제일 앞에 넣는다

# 남은 카드 하나를 출력
print(cards[0])
