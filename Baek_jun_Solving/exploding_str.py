import sys
sys.stdin = open('input.txt')

given = input()
explode = input()

result = given.replace(explode, '')
print(result if result else 'FRULA')
