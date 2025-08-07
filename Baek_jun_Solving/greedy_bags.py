N = int(input())

bags = N // 5
remainders = N % 5

while bags >= 0 and remainders > 0:
    if remainders % 3 == 0:
        bags += (remainders // 3)
        remainders = 0

    else:
        bags -= 1
        remainders += 5

print(bags)
