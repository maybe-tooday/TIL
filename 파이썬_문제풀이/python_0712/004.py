# n까지 곱하여 출력하는 코드

n = int(input())
a = 1
mul = 1

# #for문
# for a in range(1,n+1):
#     mul = mul*a
#print(mul)

#while문
while a < n + 1:
    mul = mul * a
    a += 1
print(mul)