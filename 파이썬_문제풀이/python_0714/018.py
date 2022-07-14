# 문제 18.  알파벳 등장 갯수 구하기
# ord('a') 97
# chr(97)  'a'
# 소문자a = 97 / 소문자z = 122 총 26개

word = input()
my_dict = {} #딕셔너리 정의및 초기화

for a in range(97,123):  #모두경우의 딕셔너리 생성
     my_dict[chr(a)] = 0
#{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, ... , 'w': 0, 'x': 0, 'y': 0, 'z': 0}

for c in word: 
    for a in range(97,123): 
        if c == chr(a):    #word에서 나온 c가 무슨 단어니?
            my_dict[c] += 1

for key in list(my_dict.keys()): #값이0인 키값 모두 삭제
    if my_dict[key] == 0:
        del my_dict[key] 
print(my_dict)