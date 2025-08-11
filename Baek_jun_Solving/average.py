N = int(input())   # 시험 본 과목 개수 N

scores = list(map(int, input().split()))

scores_greatest = max(scores)

for i in range(N):
    scores[i] = (scores[i] / scores_greatest) * 100

new_avg = sum(scores) / N

print(new_avg)
