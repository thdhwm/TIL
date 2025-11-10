import sys
sys.stdin = open('input.txt')

# dpdp....


str1 = [0] + list(input())  # 1-base idx
str2 = [0] + list(input())  # 1-base idx

len_1 = len(str1)    # length of 1st str
len_2 = len(str2)    # length of 2nd str

array = [['' for _ in range(len_1)] for _ in range(len_2)]    # 1st str * 2nd str matrix

for i in range(1, len_2):
    for j in range(1, len_1):
        if str1[j] == str2[i]:
            array[i][j] = array[i-1][j-1] + str1[j]
        else :
            if len(array[i][j-1]) > len(array[i-1][j]):
                array[i][j] = array[i][j-1]
            else :
                array[i][j] = array[i-1][j]

answer = len(array[-1][-1])
print(answer)
if answer != 0:
    print(array[-1][-1])
