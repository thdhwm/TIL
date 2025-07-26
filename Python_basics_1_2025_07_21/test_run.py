
for n in range(10):


    def even():
        if n % 2 == 1:
            return True, n
        else:
            return False, n
    
    if even() == True:
        print(f'{n}은/는 홀수입니다')
    else:
        print(f'{n}은/는 짝수입니다')
