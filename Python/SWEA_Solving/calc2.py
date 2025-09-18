import sys
sys.stdin = open('input.txt')

priority = {'+': 1, '*': 2}


def infix_to_postfix(tokens):
    stack = []
    oper_stack = []

    for token in tokens:
        if token.isdigit():
            stack.append(token)

        else:
            while oper_stack and priority[oper_stack[-1]] >= priority[token]:
                stack.append(oper_stack.pop())

            oper_stack.append(token)

    while oper_stack:
        stack.append(oper_stack.pop())

    return stack


def calculate(tokens):
    stack = []

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))

        else:
            num1 = stack.pop()
            num2 = stack.pop()

            if token == '+':
                stack.append(num1 + num2)
            else:     # '*' 경우
                stack.append(num1 * num2)

    return stack[0]


for tc in range(1, 11):
    N = int(input())
    formula = input()
    postfix = infix_to_postfix(formula)
    result = calculate(postfix)
    print(f'#{tc} {result}')
