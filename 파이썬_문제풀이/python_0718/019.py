# 문제 19. 숫자의 길이 구하기
# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 

a = int(input('양의 정수:'))
count = 1 #한자리 수

while a > 9 :
    a = a // 10 #10나누기 몫만 취하여 자리수를 계산한다
    count += 1

print(count,type(count))