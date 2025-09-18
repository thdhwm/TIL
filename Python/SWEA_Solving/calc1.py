import sys
sys.stdin = open('input.txt')


def infix_to_postfix(tokens):
    stack = []                   # 후위표기법 최종 결과
    oper_stack = []              # 연산자들이 중간에 거쳐갈 스택

    for token in tokens:
        # 1. 숫자라면, 그냥 stack 에 쌓기
        if token.isdigit():
            stack.append(token)

        else:
            if oper_stack:
                stack.append(oper_stack.pop())
            oper_stack.append(token)

    stack.append(oper_stack.pop())

    return stack


# 2. 후위표기법을 계산하는 함수


def calculate(tokens):
    stack = []

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            num1 = stack.pop()
            num2 = stack.pop()

            stack.append(num1 + num2)

    return stack[0]


for t in range(1, 11):
    length = int(input())
    row = list(input())
    postfix = infix_to_postfix(row)
    result = calculate(postfix)
    print(f'#{t} {result}')
