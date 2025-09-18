A, B = input().split()

A = ''.join(list(reversed(A)))
B = ''.join(list(reversed(B)))

A = int(A)
B = int(B)

print(max(A, B))


