T = int(input())

for t in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    cost_A = W * P
    if W <= R:
        cost_B = Q
    
    else:
        cost_B = Q + S * (W - R)

    final_cost = min(cost_A, cost_B)
    
    print(f'#{t} {final_cost}')
