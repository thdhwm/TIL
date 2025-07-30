# 해시함수 구현해보기
bucket = [0] * 8  # 0 데이터로 모두 들어간 8칸짜리 리스트
bucket_size = 8
# 충돌이 너무 많이 발생하는, 안좋은 해시 함수
# - 나중에는 충돌이 없도록 해시함수를 구현해야 한다.
# - 해시충돌: 다른 key 값이 같은 hash 값을 가지는 경우
def simple_hash(word):
    # a=1, b=2, c=3, ... z=26
    word = word.lower() # 모두 소문자로 처리할 것
    hash_value = 0

    for char in word:
        hash_value += ord(char) - 96
    
    return hash_value % bucket_size


print(simple_hash("abc"))
print(simple_hash("f"))
print(simple_hash("bbb"))
print(simple_hash("aaaaaa"))

# -------------------- 아스키 코드

# 컴퓨터가 a를 알까 ?
# - 숫자밖에 모른다!
# - a 라는 문자는 숫자 N이다 이렇게 정해줘야 되지 않을까 ?
#   - 아스키코드

# ord(): 문자를 아스키코드로 변환하여 출력
print(ord("a"))
print(ord("b"))
# chr(): 아스키코드 -> 문자로 변환
print(chr(97))

# 소문자 a~z 를 순서대로 출력해라
for w in range(ord("a"), ord("z") + 1):
    print(chr(w), end='')

print()
print(hash("a"))

# -------------------- 메모리

# 정수 = 21억을 잘 넘지 않는다
# - C언어: 정수 - 4bytes = 32bit
# 0000 0000 0000 0000 0000 0000 0000 0000

# 파이썬은 그냥 엄청 큰 값을 저장해도 된다.
# - 부족하면 bit 수를 늘린다
# - 그래서 느리다.
num = 3333333333333333333333333
print(num)