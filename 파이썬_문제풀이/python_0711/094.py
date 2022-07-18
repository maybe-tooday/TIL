# 094 : [기초-리스트] 이상한 출석 번호 부르기3(py)

n = int(input())      #개수를 입력받아 n에 정수로 저장
a = list(map(int,input().split()))

# b = [] #음수와0이 없는 새로은 통
# for a_1 in a:
#     if a_1 > 0:
#         b.append(a_1) 

print(min(a))