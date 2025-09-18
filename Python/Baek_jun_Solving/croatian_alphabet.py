croatian = input()
croatian_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatian_alphabet:
    croatian = croatian.replace(i, '#')

print(len(croatian))

# str 은 불변이라는걸 기억해야함 .replace 는 새로운 문자열을 반환하는것이므로 루프마다 재할당을 해줘야함.
