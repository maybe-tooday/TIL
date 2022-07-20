# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

numbers = [0, 20, 100, 40 ]
numbers = list(set(numbers)) #중복된 숫자 없어짐

max_num_1 = numbers[0] #변수를 조건안에서 찾아서 대입하는게 좋은거 같다
max_num_2 = numbers[0] #float("-inf") : 무수히 작은수

for i in numbers:
    if i > max_num_1:
        max_num_2 = max_num_1
        max_num_1 = i
    elif i > max_num_2:
        max_num_2 = i
    else:
        continue
print('최댓값 :' + str(max_num_1) + ' 두번째로 큰값:' + str(max_num_2))