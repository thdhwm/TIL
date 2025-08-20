T = int(input())

for t in range(1, T + 1):
    K = int(input())
    S = list(input())
    index_A = []
    farthest = 0
    distance = 0

    for i in range(len(S)):      
        if S[i] == 'A':
            index_A.append(i)

    if len(index_A) < K:
        farthest = 0
    
    else:
        for i in range(len(index_A) - K + 1):
            distance = index_A[i + K - 1] - index_A[i]
            if farthest < distance:
                farthest = distance

    print(f'#{t} {farthest}')

        





