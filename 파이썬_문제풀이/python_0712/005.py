#주어진 숫자의 평균 

numbers = input('숫자입력: ').split()
#print(number, type(number), type(number[0]))
a = 0 #빈 통
#count = 0 #횟수 카운트
avr = 0 #평균값 넣을 통
#print(len(number))
for i in numbers:
    #count += 1
    a = a + int(i)
avr = a / len(numbers)
print(avr)

#sum(numbers)/len(numbers)