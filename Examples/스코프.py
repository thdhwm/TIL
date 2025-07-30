
def func3():
    # 함수 스코프 (지역변수)
    print(a, b)                #######     a, b
    x, y = 10, 20

    def func4():
        print("func4")
        print(a, b)            #######     a, b

        print(x, y)           #########   10, 20
        c = 10
    func4()

# 전역변수
a = int(input())
b = int(input())

func3()            ##################

# for i in range(10):
#     abcd = 10
# print(abcd)


# ---------------------

# x = "global"

# def outer():
#     # 전역변수의 x 를 가져다 쓰겠다
#     global x
#     x = "outer"       # outer 함수의 지역 변수
#     print("1:", x)

#     def inner():
#         x = "inner"
#         print("2:", x)

#     inner()
#     print("3:", x)

# outer()
# print("4:", x)

# # ----------------------
# # 리스트를 파라미터로 전달하면 원본 값이 변경된다.
# def func5(li):
#     li[0] = 10  # 원본 li의 값도 변경됨
#     print(li)

# arr = [1, 2, 3]
# func5(arr)
# print(arr) # [10, 2, 3]


# def func6():
#     # li 라는 지역변수를 새로 만듦 (원본 li 는 수정안됨)
#     li = [4, 5, 6] # 선언
#     print(li)

# li = [1, 2, 3]
# func5()
# print(li)
