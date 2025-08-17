import sys
sys.stdin = open('input.txt')

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하기
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
N, M = map(int, input().split())
set_to_print = []


def recur(n, m):
    for num in range(1, n + 1):
        for length in range(m):
            pass





