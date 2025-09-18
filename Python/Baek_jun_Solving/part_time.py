n, x = map(int, input().split())
visitors = list(map(int, input().split()))
max_visitors = sum(visitors[:x])
sum_x = sum(visitors[:x])
count_max = 1

for i in range(n - x):
    sum_x -= visitors[i]
    sum_x += visitors[i + x]
    if max_visitors < sum_x:
        count_max = 1
        max_visitors = sum_x

    elif max_visitors == sum_x:
        count_max += 1

if max_visitors == 0:
    print('SAD')
else:
    print(max_visitors)
    print(count_max)
