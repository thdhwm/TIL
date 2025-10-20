N = int(input())

seq = list(map(int, input().split()))
reverse_seq = seq[::-1]

increasing = [1 for i in range(N)]    # 가장 긴 증가하는 부분 수열
decreasing = [1 for i in range(N)]    # 가장 긴 감소하는 부분 수열(reversed)

for i in range(N):    # 시복잡 NlogN,  N 은 max 1000
    for j in range(i):
        if seq[i] > seq[j]:    # 현 숫자보다 idx 작은거 중 증가하는 부분 수열 만족하는 것 길이 찾기
            increasing[i] = max(increasing[i], increasing[j]+1)
        if reverse_seq[i] > reverse_seq[j]:    # 리스트 뒤집은거에서 똑같이 하면 감소하는 부분 수열 만족하는 것
            decreasing[i] = max(decreasing[i], decreasing[j]+1)

result = [0 for i in range(N)]    # 각 점을 pivot으로 했을때 부분 수열 길이 봐서
reverse_decreasing = decreasing[::-1]
for i in range(N):
    result[i] = increasing[i] + reverse_decreasing[i] - 1    # pivot이 2번 들어가니까 -1

print(max(result))    # 제일 긴거가 정답!

