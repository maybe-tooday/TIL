
word = input()
char = '' #문자열 빈통

for i in word:
    if i != 'a':
        char = char + i
        print(i)
    
print(char)