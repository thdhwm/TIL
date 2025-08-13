def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start    # 피벗 초기값은 첫번째 요소 idx
    left = start + 1    # idx
    right = end    # idx

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left][1] <= array[pivot][1]:
            left += 1

            # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right][1] >= array[pivot][1]:
            right -= 1

        if left > right:  # 엇갈렸다면 작은 right -=1 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]

        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


N = int(input())    # 회의 수
table = [[0, 0] for _ in range(N)]    # time table
total = 0
fastest = 0

for i in range(N):
    table[i] = list(map(int, input().split()))          # table input done

quick_sort(table, 0, len(table) - 1)


fastest = table[0][1]
total += 1

for i in range(N):
    if table[i][0] < fastest:    # if it's past starting time, continue
        continue
    else:
        fastest = table[i][1]
        total += 1

print(total)

# ########### time out error - need more efficent sorting algorithm ################ #
