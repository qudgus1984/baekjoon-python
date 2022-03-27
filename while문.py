# -*- coding: utf-8 -*-
# ���� �˰����� 10952

from hashlib import new

while True:
    A,B = map(int ,input().split())
    if A == 0 and B == 0:
        break
    print(A+B)

# ���� �˰����� 10951

while True:
    try :
        A,B = map(int ,input().split())
        print(A+B)
    except :
        break

# ���� �˰����� 1110

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

# 2774
t = int(input())

for _ in range(t):  
    floor = int(input())  # 층
    num = int(input())  # 호
    f0 = [x for x in range(1, num+1)]  # 0층 리스트
    for k in range(floor):  # 층 수 만큼 반복
        for i in range(1, num):  # 1 ~ n-1까지 (인덱스로 사용)
            f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
    print(f0[-1])  # 가장 마지막 수 출력
        
        