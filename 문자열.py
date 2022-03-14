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
    
# 백준 알고리즘 1152

word = input().split()
print(len(word))

# 백준 알고리즘 2098

a,b = list(input().split())
list_a = list(str(a))
list_a.reverse()
a_reverse = "".join(list_a)
list_b = list(str(b))
list_b.reverse()
b_reverse = "".join(list_b)
if a_reverse > b_reverse:
    print(a_reverse)
else:
    print(b_reverse)
    
# 백준 알고리즘 5622

word = input()
time = 0
for i in word:
    if i in 'ABC':
        time += 3
    elif i in 'DEF':    
        time += 4
    elif i in 'GHI':    
        time += 5
    elif i in 'JKL':    
        time += 6
    elif i in 'MNO':    
        time += 7
    elif i in 'PQRS':    
        time += 8
    elif i in 'TUV':    
        time += 9
    elif i in 'WXYZ':    
        time += 10
print(time)
    

