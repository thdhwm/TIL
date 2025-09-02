import sys
sys.stdin = open('input.txt')


def find(parent, a):
    return


def union(parent, rank, a, b):
    return


N, M = map(int, input().split())    # n - num of people, m - num of parties
nKnow, *knows = map(int, input().split())
parent = [i for i in range(N + 1)]    # parent 가 knows 면 lying 불가능
parent_knows = [i for i in range(nKnow)]
rank = [0] * (N + 1)    # union by rank 하기 위하여
is_knowing = 0
# knows = []

for _ in range(M):
    nPeople, *people = map(int, input().split())
    
