from ws_4_list import user_data
from ws_4_list import blood_types
from ws_4_list import black_list
from pprint import pprint as print

user_list = []
error_type = []
# error_case = 0  여기 있었다가 에러 나서

def create_user():
    error_case = 0        # 여기로옴...
    def is_validation(data):

            if data['company'] in black_list:               #  blocked 인 경우 다른거 안보고 나오기
                error_type.append('blocked')
                return False, error_type
            else:                                                                   # 나머지 평가
                if data['blood_group'] in blood_types:
                    if '@' in data['mail']:
                        if len(data['name']) >= 2 and len(data['name']) <= 30:
                            if len(data['website']) >= 1:
                         
                                return True
                            
                            else:                             
                                error_type.append('website')

                        else:                          
                            error_type.append('name')
                    else:                       
                        error_type.append('mail')
                else:
                    error_type.append('blood_group')

            return False, error_type

    for data in user_data:                                      
        if is_validation(data) != True:
            if 'blocked' in is_validation(data)[1]:
                error_case += 1

            else:
                for i in range(len(error_type)):
                    data[error_type[i]] = None
                user_list.append(data)
                error_case += 1

        else:
            user_list.append(data)
    
    print(f'잘못된 데이터로 구성된 유저의 수는 {error_case}입니다')
    print(user_list)

create_user()


# blood_group의 값이 blood_types에 포함되어 있는가.    ok
# company의 값이 black_list에 포함되어 있지 않은가.    ok
# mail의 값에 @ 문자열이 포함되어 있는가.               ok
# name의 값의 길이가 최소 2글자 이상 최대 30글자 이하인가.   ok
# website가 최소 1개 이상 있는가.                         ok
# 만약, 하나라도 잘못된 값이 있다면 False를 반환하고, 어떤 데이터가 잘못 기록되었는지도 함께 반환한다. 2개 이상의 데이터가 잘못 되었다면 리스트 형태로 목록을 반환한다. 모두 정상이라면 True를 반환한다.
# 반환 예시) (False, ['blood_group', 'name'])


# create_user는 하나의 리스트를 인자로 넘겨받기

# 넘겨받은 사용자 목록을 순회하며 각각 올바른 데이터로 이루어져있는지 확인하기 위해 is_validation 함수를 구성하고 확인한다.

# 단, black_list에 company가 포함된 경우에는 'blocked' 를 반환하고, 검사를 종료한다.


# create_user는 is_validation 함수의 반환 결과를 토대로 새로운 사용자 목록 user_list를 생성한다.

# 이때, 반환 받은 값이 False인 경우, 잘못된 데이터에는 None을 할당하여 데이터를 생성한다.

# 또한, 반환 받은 값이 False이거나 'blocked'인 경우를 모두 세어, '잘못된 데이터로 구성된 유저의 수는 {개수} 입니다.' 를 출력한다.

# 단,'blocked'가 반환된 경우, 해당 유저 정보는 user_list에 추가하지 않는다.

# 완성된 user_list를 출력한다.



