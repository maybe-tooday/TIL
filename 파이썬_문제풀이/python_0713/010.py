# 주어진 리스트의 요소 중에서 5의 개수를 출력하시오.

numbers = list(map(int,input().split()))
count = 0
#print(numbers, type(numbers))

for i in numbers:
    if i == 5:
        count = count + 1
        print(count, i)

print(count)
