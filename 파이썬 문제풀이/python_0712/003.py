#sum()함수 없이 더하기

n = int(input()) #숫자 입력
a = 0 #임시 통
sum = 0 #1부터 n까지 합을 더한 숫자

# for문으로 
# for a in range(n+1):
#     sum = sum + a    
# print(sum)

# whlie문으로
while a < n :
    a = a + 1
    sum = sum + a
print(sum)  