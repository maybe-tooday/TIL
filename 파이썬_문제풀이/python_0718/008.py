word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u": #조건문 재대로 쓰기
        count += 1

print(count)