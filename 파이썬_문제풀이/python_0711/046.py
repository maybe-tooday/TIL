# 6046 : [기초-비트시프트연산] 정수 1개 입력받아 2배 곱해 출력하기(설명)(py)

n = int(input())
print(f'{n<<1}')

# 왼쪽 비트시프트(<<)가 될 때에는 오른쪽에 0이 주어진 개수만큼 추가되고,
# 오른쪽 비트시프트(>>)가 될 때에는 왼쪽에 0(0 또는 양의 정수인 경우)이나 
# 1(음의 정수인 경우)이 개수만큼 추가되고, 가장 오른쪽에 있는 1비트는 사라진다.
