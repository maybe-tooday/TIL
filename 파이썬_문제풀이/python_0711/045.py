# 6045 : [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기(설명)(py)

a, b, c = map(int,input("정수 3개 입력:").split())
d = a + b + c
e = d/3
print(d, format(e,".2f"))