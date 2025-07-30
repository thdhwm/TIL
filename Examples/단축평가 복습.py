item1 = "지도"
item2 = ""


print(item1 and item2) # "" 출력
print(item1 or item2)  # "지도" 출력
print((item1 and item2) == False) # False
print((item1 and item2) == "") # True
print("" == False)  # False

if "": # 조건문에서는 False 로 인식
    print("값이 비어있다")

print(item1 or item2)