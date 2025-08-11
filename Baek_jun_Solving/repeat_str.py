T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    S = list(S)
    repeated_list = []

    for i in range(len(S)):
        repeated_list.append(R * S[i])

    print(''.join(repeated_list))


