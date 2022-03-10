# 백준 알고리즘 1330

A,B = map(int, input().split(" "))
if A > B :
    print(">")
elif A < B :
    print("<")
elif A == B :
    print("==")
    
# 백준 알고리즘 9498

X = int(input())
if X >= 90 :
    print("A")
elif X >= 80 :
    print("B")
elif X >= 70 :
    print("C")
elif X >= 60 :
    print("D")
else :
    print("F")

# 백준 알고리즘 2753

year = int(input())
if year%4 == 0 and year%100 != 0:
    print(1)
elif year%400 == 0:
    print(1)
else:
    print(0)

# 백준 알고리즘 14681

x = int(input())
y = int(input())
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)

# 백준 알고리즘 2884

H,M = map(int, input().split())
M = M-45

if M < 0 and H != 0:
    H = H-1
    M = M+60
    print(H,M)
elif M < 0 and H == 0:
    H = H+23
    M = M+60
    print(H,M)
else:
    print(H,M)

# 백준 알고리즘 2525

H,M = map(int, input().split())
C = H*60 + M + int(input())
print(C//60%24,C%60)

# 백준 알고리즘 2480

a,b,c=map(int,input().split())

if a==b==c:
    print(10000+a*1000)
elif a==b: 
    print(1000+a*100)
elif a==c:
    print(1000+a*100)
elif b==c:
    print(1000+b*100)
else:
    print(100*max(a,b,c))
