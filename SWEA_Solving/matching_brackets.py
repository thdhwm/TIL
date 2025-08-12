for t in range(1, 11):
    N = int(input())
    brackets = list(input())
    stack = []
    validation = True

    if N % 2 == 1:
        print(f'#{t} 0')   # 홀수 갯수 괄호 불가능
        continue

    for bracket in brackets:
        if bracket == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                validation = False
                break

        elif bracket == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                validation = False
                break

        elif bracket == '}':
            if len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            else:
                validation = False
                break

        elif bracket == '>':
            if len(stack) > 0 and stack[-1] == '<':
                stack.pop()
            else:
                validation = False
                break

        else:
            stack.append(bracket)

    if len(stack) > 0:
        validation = False

    if validation:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
