# 6083 : [기초-종합] 빛 섞어 색 만들기(설명)(py)

r, g, b = map(int,input().split())
count = 0

for r_1 in range(0,r):
    for g_1 in range(0,g):
        for b_1 in range(0,b):
            print(r_1,g_1,b_1)
            count += 1
print(count)