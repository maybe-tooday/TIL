# 6085 : [기초-종합] 그림 파일 저장용량 계산하기(py)

w, h, b = map(int,input().split())

bit = w * h * b /8 /1024 /1024
bit = format(bit,'.2f')
print(f'{bit} MB')
