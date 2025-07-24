# 참인경우 값 if 조건 else 거짓인경우 값
# 삼항 연산자
# 참인경우 값 if 조건 else 거짓인경우 값
# print("True는 참" if True else "True는 거짓")
# print("False는 참" if False else "False는 거짓")

a, b = map(int, input().split())

if b > a:
    a, b = b, a
result = a - b

print(result)

