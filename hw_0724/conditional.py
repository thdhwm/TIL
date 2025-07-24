def step1(cm):
    
    if cm >= 140:
        print('탑승 가능합니다.')
    else:
        print('탑승 불가입니다.')

def step2(age, cm):
    if age >= 12 and cm >=140:
        print('탑승 가능합니다.')
    else:
        print('탑승 불가입니다.')

def step3(age, cm, parent):
    if cm >= 140 and age >= 12:
        print('탑승 가능 (단독)')
    elif cm >= 140 and age < 12 and parent == 'y':
        print('탑승 가능 (보호자 동반)')
    elif cm >= 140 and age < 12 and parent == 'n':
        print('혼자서는 탑승 불가')
    elif cm < 140:
        print('키 제한으로 탑승 불가')

# def step3(age, cm, parent):
#     if cm >= 140:
#         if age >= 12:
#             print('탑승 가능 (단독)')
#         else:
#             if parent == 'y':
#                 print('탑승 가능 (보호자 동반)')
#             else:
#                 print('혼자서는 탑승 불가')
#     else:
#         print('키 제한으로 탑승 불가')