# -*- coding: utf-8 -*-

# 백준 알고리즘 11654

a = ord(input())
print(a)

# 백준 알고리즘 11720

n = int(input())
num = list(map(int, str(input())))
print(sum(num))

# 백준 알고리즘 10809

n = input()
alpha = list(range(97,123)) # 아스키코드에서 a~z까지의 범위
for i in range(len(alpha)):
    print(n.find(chr(alpha[i]))) 
    
# 백준 알고리즘 2675

re = int(input()) # 반복 횟수
for i in range(re):
    num, s = input().split()
    text = ''
    for i in s:
        text += int(num) * i
    print(text)
    
# 백준 알고리즘 1157 : 가장 많이 사용된 알파벳

word = input().upper() # 모두 대문자로 변경
word_list = list(set(word)) # set 함수로 중복 제거
x = []

for i in word_list:
    count = word.count(i)
    x.append(count)
    
if x.count(max(x)) >= 2:
    print("?")
    
else:
    print(word_list[(x.index(max(x)))])
    
