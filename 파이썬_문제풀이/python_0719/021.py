number = int(input())
num = []
rev_num = 0
count = 0

#print(int(str(number)[::-1])) 

while number > 0:
    num.append(number % 10)
    number //= 10
    count += 1
    #print(number, num, count)

for i in range(count,0,-1): 
    rev_num += num[i-1] * (10**(count-i))
print(rev_num)