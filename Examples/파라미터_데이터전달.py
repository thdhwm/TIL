def func2(x, y):
    # 함수가 외부 데이터를 필요로 할 때
    # 숫자 2개를 합치는 함수
    # -> 숫자 2개는 외부에서 입력을 받았다.
    print(x + y)

def my_input():
    num1 = int(input())
    num2 = int(input())
    return num1, num2

# 1. my_input 이 입력받은 값을 반환해주고
# 2. func2 데이터를 받아서 결과를 출력
n1, n2 = my_input()
func2(n1, n2)