# 6090 : [기초-종합] 수 나열하기3(py)

a, m, d, n = map(int,input().split())
ans = 0
#a : 시작값, m : 곱할값, d : 더할값, n : 몇번쨰

for num in range(1,n+1):
    if num == 1:
        ans = a
    else :
        ans = ans * m + d
print(ans)