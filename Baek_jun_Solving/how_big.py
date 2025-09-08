import sys
sys.stdin = open('input.txt')

N = int(input())

people = []
for _ in range(N):
    weight, height = map(int, input().split())
    people.append((weight, height))

for i in range(N):
    rank = 1
    for j in range(N):
        if i != j:
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                rank += 1
    print(rank, end=" ")
# BOJ 7568