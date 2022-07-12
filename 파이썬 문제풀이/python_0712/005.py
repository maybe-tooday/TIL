#주어진 숫자의 평균 

number = [3, 10, 20]
a = 0
count = 0
avr = 0

for i in number:
    count += 1
    a = a + i
avr = a/count
print(avr)