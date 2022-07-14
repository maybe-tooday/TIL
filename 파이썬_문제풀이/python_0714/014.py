# 문자의 갯수 구하기

word = input()
count = 0 #문자 갯수 넣응 통

for i in word:
    #print(i)
    if i == 'a':
        count += 1
print(count)