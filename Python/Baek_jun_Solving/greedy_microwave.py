# a, b, c buttons exist 
# each button extends microwave time by
# 300s 60s 10s
# cooking time T  in seconds
# if T cannot be divided by a,b,c cleanly print -1

T = int(input())
button_count = [0, 0, 0]
is_10x = True
if T % 10 != 0:
    is_10x = False
    T = 0

while T > 0:
    if T >= 300:
        T -= 300
        button_count[0] += 1

    elif T >= 60:
        T -= 60
        button_count[1] += 1

    elif T >= 10:
        T -= 10
        button_count[2] += 1

if is_10x:
    print(*button_count)
else:
    print(-1)