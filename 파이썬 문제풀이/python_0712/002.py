#반복문을 활용하여 문자열 word의 길이를 출력하는 코드 작성

word = input()
a = 0 

for char in word:  #글자 길이만큼 반복하며 +1을 더한다. 즉 자릿수를 카운팅한다
    #print(char)
    a += 1

print(a)