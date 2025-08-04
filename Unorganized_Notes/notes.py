# 첫 시험 

# 객관식 코드 1개 쓰고 출력 결과 뭐 나올까요? a/b/c/d 같은거


# 재귀 함수 - 자기 자신을 호출하는 함수  -> 요정도만 해도 정답!
# 재귀 함수의 필수 구성 요소
# 1. 시작점, 누적값
# 2. 종료조건


# 재귀함수의 필수 구성 요소
# 1. 시작점, 누적값
# 2. 종료조건

# 단축 평가
# item1 = "지도"
# item2 = ""


# print(item1 and item2) # "" 출력
# print(item1 or item2)  # "지도" 출력
# print((item1 and item2) == False) # False
# print((item1 and item2) == "") # True
# print("" == False)  # False

# if "": # 조건문에서는 False 로 인식
#     print("값이 비어있다")

# print(item1 or item2)


### for와 while의 차이?
########################################################################################


arr = [2, 4, 6, 8, 10]

# 2 4 6 8 10 8 6 4 2

# 2 4 6 8 10
def func(idx):
    if idx == len(arr) - 1:
        # 종료 조건이 만족했을 때, 수행되어야 할 로직
        print(arr[idx], end=' ')    
        return
    
    print(arr[idx], end=' ')  # 다음 재귀 호출 전에 뭘 하고 싶은가 ?

    func(idx + 1)  # 다음 재귀 호출에는 어떤 값을 전달해주어야 하는가 ?

    print(arr[idx], end=' ')  # 돌아오면서는 어떤 로직을 수행하고 싶은가 ?
    
func(0)

#func(0) -> func(1) -> func(2)

# 십진수 -> 이진수로 변환 (재귀호출)
# 10 -> 1010

def binary(num):
    if num < 2:
        print(num, end='')
        return

    binary(num // 2)  # 2로 나눈 몫을 전달
    print(num % 2, end='')

binary(10)




# 역량 테스트 IM ~3주 후
# IM 난이도 단순, 쉬움







# 문자열 활용하는 알고리즘 문제에서 많이 씀
#  ord('a')  ->   문자에서 아스키 코드로
#  chr(97)   ->   아스키 코드에서 문자로




#신입들이 ai 관련 무슨 역량이 있었음 좋을까? 물어봤더니
# 모델 서빙
# 학습
# 추론 모델
# 서비스에 적용
# 인프라
# 리눅스, docker, etc.




# 다음주 월 과목평가
# 다다음 주 월 일타싸피
# 다다음 주 화 역량평가

# 문제1  (40) -> 내장함수 X
# min, max, sum 쓰지 말라 그럼
# - 다차원 리스트에서 min, max, sum 돌려보기

# 문제2 (35) - 어려운거
# 서술형 (25) - 힌트 많이 줄 예정




