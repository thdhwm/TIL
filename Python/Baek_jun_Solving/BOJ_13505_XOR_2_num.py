import sys
sys.stdin = open('input.txt')
N = int(input())

numbers = tuple(map(int, input().split()))
max_val = 0

for i in range(N):
    for j in range(i + 1, N):
        max_val = max(max_val, numbers[i] ^ numbers[j])

print(max_val)

# ######################################################################
# trie, prefix tree
