# 백준 알고리즘 10818

from calendar import c
from re import X

n = int(input())
a = list(map(int, input().split()))
print('{} {}'.format(min(a), max(a)))

# 백준 알고리즘 2562

n = []
for i in range(9):
  n.append(int(input()))

print(max(n))
print(n.index(max(n))+1)

# 백준 알고리즘 2577

a = int(input())
b = int(input())
c = int(input())
x = str(a*b*c)

for i in range(10):
  i_count = x.count(str(i))
  print(i_count)

# 백준 알고리즘 3052

n = []
for i in range(10):
  x = int(input())
  n.append(x % 42)
n = set(n)
print(len(n))

# 백준 알고리즘 1546

n = int(input())
x = list(map(int, input().split()))
sum = 0

max_x = max(x)

for i in range(n):
  sum += ((x[i] / max_x)*100)
total = sum / n
print(total)

# 백준 알고리즘 8958

n = int(input())
A = []
for i in range(n):
  O_score = 0
  X_score = 0
  Total_score = 0
  A = input()
  for B in A:
    if B == 'O':
      O_score += 1
      Total_score += O_score
    else:
      X_score = 0
      O_score = 0
  print(Total_score)

# 백준 알고리즘 4344

C = int(input())
for i in range(C):
    score = list(map(int,input().split(())))
    average = sum(score[1:])/score[0]
    count = 0
    for j in score[1:]: 
        if j > average:
            count += 1
    aver = count/score[0] * 100
    print("{:.3f}%".format(aver))

