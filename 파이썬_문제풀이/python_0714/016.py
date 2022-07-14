# 문제 16. 모음 등장 여부 확인하기

word = input()
count = 0 #모음카운터

for c in word:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        count += 1

# for c in word:
#     if c == 'a' :
#         count += 1
#     elif c == 'e' :
#         count += 1
#     elif c == 'i' :
#         count += 1 
#     elif c == 'o' :
#         count += 1
#     elif c == 'u' :
#         count += 1

print(count)