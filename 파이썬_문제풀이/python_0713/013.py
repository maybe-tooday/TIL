# 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.


word = input()
word_rev = ''

for i in word:
    word_rev =  i + word_rev 
    #print(word_rev)

print(word)
print(word_rev)

# 2.pythonic
#print(word[::-1])
#print(reversed(word))

# 3.index
# range(len(word))
# print(word[len(word)-i-1],end='')