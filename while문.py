# 백준 알고리즘 10952

from hashlib import new

while True:
    A,B = map(int ,input().split())
    if A == 0 and B == 0:
        break
    print(A+B)

# 백준 알고리즘 10951

while True:
    try :
        A,B = map(int ,input().split())
        print(A+B)
    except :
        break

# 백준 알고리즘 1110

n = int(input())
new = n
i = 0
while True:
    a = new // 10
    b = new % 10
    c = (a+b) % 10
    new = 10*b + c
    i = i+1
    if (n==new):
        break
print(i)

        
        