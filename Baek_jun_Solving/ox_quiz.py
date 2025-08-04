T = int(input())

for t in range(1, T + 1):
    quiz = list(input())
    total = 0
    score = 0

    for i in range(len(quiz)):
        if quiz[i] == 'O':
            score += 1
            total += score                      #O면 스코어 만큼 더하고 스코어 +1

        else:
            score = 0                      #x면 스코어 초기화

    print(total)    
    