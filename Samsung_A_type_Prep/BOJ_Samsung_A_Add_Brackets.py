import sys
sys.stdin = open('../../Baek_jun_Solving/input.txt')

N = int(input())
formula = input().strip()
max_outcome = -2**31
# #######################################################
def calc(n1, n2, operator):    # 연산, '+', '-', '*' 우선순위 동일
    if operator == '+':
        return n1 + n2
    elif operator == '-':
        return n1 - n2
    elif operator == '*':
        return n1 * n2

def dfs(idx, current_value):    # idx - 갯수  # 현 위치(숫자)
    global max_outcome

    if idx == len(formula):
        max_outcome = max(max_outcome, current_value)
        return

    next_value = calc(current_value, int(formula[idx + 1]), formula[idx])
    dfs(idx + 2, next_value)

    if idx + 4 <= len(formula):
        bracket = calc(int(formula[idx + 1]), int(formula[idx + 3]), formula[idx + 2])
        next_value = calc(current_value, bracket, formula[idx])
        dfs(idx + 4, next_value)


# ########################################################
dfs(1, int(formula[0]))

print(max_outcome)