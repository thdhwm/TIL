S = input()
suffix = []
for i in range(len(S)):
    suffix.append(S[i:])

suffix.sort()

# for i in range(len(S)):
#     if i + 1 < len(S) and suffix[i][0] == suffix[i + 1][0]:
#         length = min(len(suffix[i]), len(suffix[i + 1]))
#         for k in range(length):
#             if ord(suffix[i][k]) > ord(suffix[i + 1][k]):
#                 suffix[i], suffix[i + 1] = suffix[i + 1], suffix[i]
#                 break

for i in range(len(S)):
    print(suffix[i])

