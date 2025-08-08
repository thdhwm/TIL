T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    answer_sheet = list(map(int, input().split()))
    student_answers = [[0] * M for _ in range(N)]
    max_score = 0
    min_score = 100

    for i in range(N):
        student_answers[i] = list(map(int, input().split()))

####################### 입력 받기 끝  ###########################

    for i in range(N):
        student_score = 0
        score = 0
        for j in range(M):
            if answer_sheet[j] == student_answers[i][j]:
                score += 1
                student_score += score

            else:
                score = 0

        if max_score < student_score:
            max_score = student_score

        if min_score > student_score:
            min_score = student_score

    diff = max_score - min_score

    print(f'#{t} {diff}')

# 16 min.
# pass in 1 go
