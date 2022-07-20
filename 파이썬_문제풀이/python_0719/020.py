number = int(input())
sum_num = 0

while number > 0:
    sum_num += number%10
    number //= 10
# divmod(x,y)는 x를 y로 나누고,
# 결과를 tuple로 반환
# (몫, 나머지)

print(sum_num)  