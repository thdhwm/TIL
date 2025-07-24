arr = [2, 3, 4, 5, 6]

# for i in arr:
#     print(i, end=' ')
# print()

# for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#         print (arr[i], end=' ')
# print()


# for i in range(5):
#     for j in range(5):
#         pass
#     print()

# 정수 n 에 대해
# 1+ 2+ 3+ ... 하다가
# 누적합이 n 이상이면 중지
# 그때 마지막 숫자
def last_num(n):
    sum = 0
    for i in range(1, n + 1):
        if sum >= n:
            last = i - 1
            break
        else:
            sum += i
    return last
print(last_num(10))


# def solution(n):
#     total = 0 # 누적합
#     now = 1 # 1 부터 증가할 변수
    
#     while total < n:
#         total += now
#         now += 1

#     print(f'누적 합이 {n} 이상이 된 시점 마지막 숫자 = {now - 1}')
# solution(10)