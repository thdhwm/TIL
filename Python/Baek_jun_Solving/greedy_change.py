charge = int(input())
pay = 1000 - charge
change = 0
while pay > 0:
    if pay >= 500:
        pay -= 500
        change += 1
    
    elif pay >= 100:
        pay -= 100
        change += 1

    elif pay >= 50:
        pay -= 50
        change += 1

    elif pay >= 10:
        pay -= 10
        change += 1

    elif pay >= 5:
        pay -= 5
        change += 1

    elif pay >= 1:
        pay -= 1
        change += 1

print(change)

