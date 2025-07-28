# 1. 모듈과 패키지
# - 다른 파일의 코드를 가져와서 써보자

# - 코드 분리
#   - 1. 함수로 기능 별로 분리
#   - 2. 파일로 분리

# 다른 파일에 있는 코드를 가져오는 방법
# 1. 모듈(파이썬 파일)을 import 하는 방법
# - 내가 쓰지 않는 기능들도 모두 import
import first
# func() # 전역의 func, first 의 func 알 수 없다.
first.func()

def func():
    print("main 의 func 호출")
    
# 2. 필요한 기능들만 가져오자
# - as(alias): 별명을 지어주는 개념
from first import func as first_func

func()  # main.py 에서 정의한 함수
first_func()  # first 모듈에서 정의한 함수
