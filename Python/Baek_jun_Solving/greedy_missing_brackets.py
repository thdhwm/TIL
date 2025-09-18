equation = list(input())    # 10+20+30+40  형식 입력값
digit_5 = [0] * 5    # 5자리보다 많이 연속되는 숫자는 없다
digit = 0
num_in_equation = []
positive_index = 0
positive_total = 0
negative_total = 0


def digit_to_num(arr):
    number = 0
    for i in range(len(arr)):
        number += arr[i] * (10 ** i)

    return number


for char in equation[::-1]:

    if char == '+':
        num_in_equation.append(digit_to_num(digit_5))
        digit_5 = [0] * 5
        digit = 0

    elif char == '-':
        num_in_equation.append(-digit_to_num(digit_5))
        digit_5 = [0] * 5
        digit = 0

    else:
        digit_5[digit] = int(char)
        digit += 1

num_in_equation.append(digit_to_num(digit_5))    # 마지막 숫자 리스트에 더해주기
refined_equation = num_in_equation[::-1]

if '-' in equation:
    for i in range(len(refined_equation)):
        if refined_equation[i] < 0:
            positive_index = i - 1
            break

    for i in range(0, positive_index + 1):
        positive_total += refined_equation[i]

    for i in range(positive_index + 1, len(refined_equation)):
        negative_total += abs(refined_equation[i])

    final_total = positive_total - negative_total

else:
    final_total = sum(refined_equation)

print(final_total)
