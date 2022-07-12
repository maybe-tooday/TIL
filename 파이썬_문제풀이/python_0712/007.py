#주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
#min() 함수 사용 금지

number = [10, 20, 30]
min = 0 #최솟값
a = 0 #계산 카운팅

for i in number:
    if a==0:
        min=i
    else:
        if min>i:
            min=i
    a+=1
print(min, a)