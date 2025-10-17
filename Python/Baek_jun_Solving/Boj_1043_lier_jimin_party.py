import sys
sys.stdin = open('input.txt')
#
#
# def find(parent, a):
#     return
#
#
# def union(parent, rank, a, b):
#     return
#
#
# N, M = map(int, input().split())    # n - num of people, m - num of parties
# nKnow, *knows = map(int, input().split())
# parent = [i for i in range(N + 1)]    # parent 가 knows 면 lying 불가능
# parent_knows = [i for i in range(nKnow)]
# rank = [0] * (N + 1)    # union by rank 하기 위하여
# is_knowing = 0
# # knows = []
#
# for _ in range(M):
#     nPeople, *people = map(int, input().split())
#
# # #########################################


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 경로 압축
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 입력
N, M = map(int, input().split())  # 사람 수, 파티 수
T, *truth = list(map(int, input().split()))  # 진실 아는 사람 수와 번호

parties = []  # 파티별 참석자 리스트
for _ in range(M):
    P, *party = list(map(int, input().split()))
    parties.append(party)  # 참석자 번호만 저장

parent = list(range(N + 1))  # 사람 1~N의 부모 배열

# 진실 아는 사람 그룹화
if T > 0:
    truth_root = truth[0]  # 진실 그룹의 대표 (첫 번째 진실 아는 사람)
    for person in truth:
        union(parent, truth_root, person)  # 진실 아는 사람을 같은 그룹으로

# 파티별로 사람들 그룹화
for party in parties:
    if len(party) > 1:
        for i in range(1, len(party)):
            union(parent, party[0], party[i])  # 첫 번째 사람과 나머지 사람 묶기

# 과장된 이야기 가능한 파티 수 세기
answer = 0
for party in parties:
    can_lie = True
    for person in party:
        if T > 0 and find(parent, person) == find(parent, truth_root):
            can_lie = False
            break

    if can_lie:
        answer += 1

print(answer)
