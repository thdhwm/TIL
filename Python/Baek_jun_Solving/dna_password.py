S, P = map(int, input().split())    # ex. 9 8
DNA = list(input())     # ex. CCTGGATTG
at_least = list(map(int, input().split()))     # ex. 2 0 1 1
ACGT = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
count_password = 0

for i in range(P):
    ACGT[DNA[i]] += 1

password = list(ACGT.values())
is_password = 0
for least in range(4):
    if password[least] < at_least[least]:
        is_password = 0
        break
    else:
        is_password = 1

if is_password:
    count_password += 1


for j in range(S - P):    # 1번
    ACGT[DNA[j]] -= 1     # 0번 뺴고
    ACGT[DNA[P + j]] += 1   # 8번 더하고
    password = list(ACGT.values())
    is_password = 0

    for least in range(4):
        if password[least] < at_least[least]:
            is_password = 0
            break
        else:
            is_password = 1

    if is_password:
        count_password += 1

print(count_password)




