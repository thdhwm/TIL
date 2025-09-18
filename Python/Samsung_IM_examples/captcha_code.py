T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    sample_list = list(map(int, input().split()))
    pass_code = list(map(int, input().split()))
    is_possible = 0

    sample_index = 0
    code_index = 0
    while sample_index < len(sample_list) and code_index < len(pass_code):
        if pass_code[code_index] == sample_list[sample_index]:
            code_index += 1
            sample_index += 1

        else:
            sample_index += 1

    if code_index == len(pass_code):
        is_possible = 1

    print(f'#{t} {is_possible}')

# 15 min.
# pass in 1 go
