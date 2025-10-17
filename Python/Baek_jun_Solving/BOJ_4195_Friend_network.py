"""
첫째 줄에 테스트 케이스의 개수가 주어진다.
각 테스트 케이스의 첫째 줄에는 친구 관계의 수 F가 주어지며,
이 값은 100,000을 넘지 않는다.
다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어진다.
친구 관계는 두 사용자의 아이디로 이루어져 있으며,
알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열이다.

출력
친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.
"""
import sys
sys.stdin = open('input.txt')
def find(parent, a):
    root = a

    while parent[root] != root:
        root = parent[root]

    while parent[a] != a:
        next_node = parent[a]
        parent[a] = root
        a = next_node

    return root


def union(parents, new, a, b):
    parents_a = find(parents, a)
    parents_b = find(parents, b)

    if parents_a < parents_b:
        count_list[parents_a] += count_list[parents[parents_b]]
        parents[parents_b] = parents_a
        count_list[parents_a] += new
        return count_list[parents_a]
    else:
        count_list[parents_b] += count_list[parents[parents_a]]
        parents[parents_a] = parents_b
        count_list[parents_b] += new
        return count_list[parents_b]


T = int(input())
for _ in range(T):
    F = int(input())

    indices = {}
    parents = [n for n in range(200001)]
    count_list = [0] * 200001

    nPeople = 0
    for f in range(F):
        friend_A, friend_B = input().split()
        new_comer = 0
        if indices.get(friend_A, 'not_found') == 'not_found':
            nPeople += 1
            new_comer += 1
            indices[friend_A] = nPeople

        if indices.get(friend_B, 'not_found') == 'not_found':
            nPeople += 1
            new_comer += 1
            indices[friend_B] = nPeople

        print(union(parents, new_comer, indices[friend_A], indices[friend_B]))