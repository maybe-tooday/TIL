# 주어진 리스트가 반장 선거 투표 결과일 때 이영희의 총 득표수를 출력하시오.

students = input('이영희, 김철수, 조민지 :').split()
count = 0

for i in students:
    if i == '이영희':
        count = count + 1
        #print(count,type(i))
    # else:
    #     continue
print(count)