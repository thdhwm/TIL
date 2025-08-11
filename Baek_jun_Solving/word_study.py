S = input()
S = S.lower()
chr_in_S = list(set(S))
num_char = [0] * len(chr_in_S)
most_often = 0
idx_most_often = 0

for i in range(len(chr_in_S)):
    num_char[i] = S.count(chr_in_S[i])
    if most_often < S.count(chr_in_S[i]):
        most_often = S.count(chr_in_S[i])
        idx_most_often = i

if num_char.count(most_often) > 1:
    print('?')

else:
    print(chr_in_S[idx_most_often].upper())
