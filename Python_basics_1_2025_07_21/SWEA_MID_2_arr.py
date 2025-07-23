T = int(input())

for t in range(1, T + 1):
    
    size = int(input())
    arr = []
    spin_90, spin_180, spin_270 = []
    trans_list_90, trans_list_180, trans_list_270 = []

    for i in range(size):
        
        arr.append(list(map(int, input().split()))) #행렬 설정 끝


    for i in range(size):
        for j in range(size):       #arr[i][j]
            spin_90.append(arr[j][size - i - 1])
    
    final_product_90 = spin_90[: : -1]   #90도 회전 후 행렬 리스트 형태로
    
    for i in range(size):
        trans_list_90.append(final_product_90[(size * i) : (size * i + size)])   # 2중 행렬 형태로 정렬 완료

  #180도 반복

    for i in range(size):
        for j in range(size):       #arr[i][j]
            spin_180.append(trans_list_90[j][size - i - 1])
    
    final_product_180 = spin_180[: : -1]

    for i in range(size):
        trans_list_180.append(final_product_180[(size * i) : (size * i + size)])

# 270도 반복

    for i in range(size):
        for j in range(size):       #arr[i][j]
            spin_270.append(trans_list_180[j][size - i - 1])
    
    final_product_270 = spin_270[: : -1]

    for i in range(size):
        trans_list_270.append(final_product_270[(size * i) : (size * i + size)])

#출력 시작
    print(f'#{t}')
    for i in range(size):
        print(
        ''.join(str(num) for num in trans_list_90[i]) + ' ' +
        ''.join(str(num) for num in trans_list_180[i]) + ' ' +
        ''.join(str(num) for num in trans_list_270[i])
    )



# for i in range(size):
#     print(f'{trans_list_90[i]} {trans_list_180[i]} {trans_list_270[i]}')