T = int(input())

for t in range(1, T + 1):
    N, M1, M2 = map(int, input().split())
    blocks = list(map(int, input().split())) # N 개의 블록

    block_count = 0
    stack_A = 1
    stack_B = 1
    total_M1 = 0
    total_M2 = 0
    sorted_blocks = sorted(blocks, reverse = True)

    while block_count < N:   # 5
        if stack_A <= M1:   # 3
            total_M1 += (stack_A) * sorted_blocks[block_count]
            block_count += 1
            stack_A += 1
        
        if stack_B <= M2:   # 2
            total_M2 += (stack_B) * sorted_blocks[block_count]
            block_count += 1
            stack_B += 1
    
    print(f'#{t} {total_M1 + total_M2}')