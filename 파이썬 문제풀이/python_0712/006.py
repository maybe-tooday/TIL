from re import A


numbers = [0, 20, 100, 50, -60, 50, 100]
max = 0 #더 큰변수

for i in numbers:
    if max<i :
        max=i
print(max)