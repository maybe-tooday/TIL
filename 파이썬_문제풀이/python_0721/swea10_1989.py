# 1989. 초심자의 회문 검사 D2

T = int(input())

for t in range(1, T + 1):
    word = input()
    word_rev = word[::-1]
    #for chr in word:  #word단어를 하나씩 앞에 넣어서 먼저넣은 단어가 뒤로가면서 역순이 된다
    #    word_rev = chr + word_rev
    print(f'#{t} {int(word==word_rev)}')
    #print(word, word_rev)
