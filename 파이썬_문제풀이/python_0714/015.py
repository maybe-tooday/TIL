# 문제 15. 문자의 위치 구하기

word = input()
count = 0   #특정 문자 위치(인덱스)값
result = '' #결과값 출력통
# range(len(word))

for c in word:
    if c == 'a':
        result = result + f'{count} '
        #break
    elif result == '':
        result = '-1'
    count += 1
    

print(result)