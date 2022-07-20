# 2058. 자릿수 더하기 D1

t = int(input())
count = 0

while t > 0:
    count += t % 10
    t //= 10
print(count)