#2050. 알파벳을 숫자로 변환 D1

w = input()
num = []

for c in range(len(w)):
    print(f'{ord(w[c])-64}', end = ' ')