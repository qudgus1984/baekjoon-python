# 백준 알고리즘 2739

N = int(input())
for i in range(1,10):
    print('{0} * {1} = {2}'.format(N,i,N*i))

# 백준 알고리즘 10950

T = int(input())
for i in range(T):
  A,B = map(int, input().split())
  print(A+B)

# 백준 알고리즘 8393

sum = 0
n = int(input())
for i in range(n+1): # 0,1,2, ... , n 까지를 의미
  sum = sum+i
print(sum)

# 백준 알고리즘 15552

import sys

T = int(sys.stdin.readline())
for i in range(T):
  A,B = map(int, sys.stdin.readline().split())
  print(A+B)

# 백준 알고리즘 2741

N = int(input())
for i in range(1, N+1):
  print(i)

# 백준 알고리즘 2742

N = int(input())
for i in range(N, 0, -1):
  print(i)

# 백준 알고리즘 11021

t = int(input())
for i in range(1, t+1):
  A,B = map(int, input().split())
  print('Case #{0}: {1}' .format(i, A+B))

# 백준 알고리즘 11022

t = int(input())
for i in range(1, t+1):
  A,B = map(int, input().split())
  print('Case #{0}: {1} + {2} = {3}' .format(i, A, B, A+B))

# 백준 알고리즘 2438

N = int(input())
for i in range(1, N+1):
  print("*"*i)

# 백준 알고리즘 2439

N = int(input())
for i in range(1, N+1):
  print(" "*(N-(i*1)),"*"*i,sep="")

# 백준 알고리즘 10871

N,X = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
  if A[i]<X:
    print(A[i] ,end="")
  