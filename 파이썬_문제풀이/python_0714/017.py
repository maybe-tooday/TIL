# 문제 17. 소문자-대문자 변환하기


word = input()
word_new = '' #대문자 넣을 통

for c in word:
    word_new = word_new + chr(ord(c)-32)

print(word_new)