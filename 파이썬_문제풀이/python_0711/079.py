# 6079 : [기초-종합] 언제까지 더해야 할까?(py)

number = int(input())
a = 1  # 계속해서 더할 숫자
b = 0  # 숫자가 더해지며 쌓일 통
while b < number:
    b += a
    a += 1
    #print(b)
print(a-1)