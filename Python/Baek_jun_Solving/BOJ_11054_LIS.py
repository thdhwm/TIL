N = int(input())

case = list(map(int, input().split()))
reverse_case = case[::-1]

increase = [1 for i in range(N)]    # 가장 긴 증가하는 부분 수열
decrease = [1 for i in range(N)]    # 가장 긴 감소하는 부분 수열(reversed)

for i in range(N):
    for j in range(i):
        if case[i] > case[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if reverse_case[i] > reverse_case[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = [0 for i in range(N)]
for i in range(N):
    result[i] = increase[i] + decrease[N-i-1] - 1    # pivot이 2번 들어가니까 -1

print(max(result))
