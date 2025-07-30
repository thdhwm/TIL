T = int(input())

for t in range(1, T + 1):
    length = int(input())
    triangle = [[0] * length for _ in range(length)]

    for i in range(length):            # N = 1, 2는 하드 코딩으로 
        triangle[i][0] = 1
        triangle[i][i] = 1
    if length > 2:                    # 2 이상이면...  (2,1) 부터
        for j in range(2, length):           #1개, 다음층 2개 ....
            for k in range(1, j):
                triangle[j][k] = triangle[j - 1][k - 1] + triangle[j -1][k]

###################################### 삼각형 행렬에 넣기 완료 ######################################

######################################  행렬에서 0 뺴고 출력  ######################################

    print(f'#{t}')
    for layer in triangle:
        result = ''
        for i in layer:
            if i > 0:
                result += str(i)
                result += ' '
        print(result)
            