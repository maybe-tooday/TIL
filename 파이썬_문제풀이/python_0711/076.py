# 6076 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기2(설명)(py)

n = int(input())
for i in range(n+1) :
  print(i)

# range(끝)
# range(시작, 끝)
# range(시작, 끝, 증감)
# 형태로 수열을 표현할 수 있다. 시작 수는 포함이고, 끝 수는 포함되지 않는다. [시작, 끝)
# 증감할 수를 작성하지 않으면 +1이 된다.