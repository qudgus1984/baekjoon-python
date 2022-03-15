# 백준 알고리즘 1712

A,B,C = map(int, (input().split())) # A는 고정비용, B는 가변비용, C는 노트북 가격
if B < C:
    print(int(A/(C-B))+1)
else:
    print(-1)

# 백준 알고리즘 2292

n = int(input()) # 입력받은 숫자
room = 1
cnt = 1
while n > room:
    room += 6*cnt
    cnt += 1
print(cnt)

# 백준 알고리즘 1193

x = int(input())
n = 1 # 대각선

while x > n:
    x -= n
    n += 1

if n % 2 == 0: # 대각선이 짝수인 경우
    up = x
    down = n - x + 1
elif n % 2 == 1: # 대각선이 홀수인 경우
    up = n - x + 1
    down = x
print(up,"/",down,sep = "")

# 백준 알고리즘 2869

a,b,v = map(int, input().split())
x = (v-a)/(a-b)+1
if (v-a)%(a-b) == 0:
    print(int(x))
else:
    print(int(x)+1)

# 백준 알고리즘 10250

t = int(input()) # 테스트 케이스
for i in range(t):
    h,w,n = map(int, input().split())
    x=n//h+1 # x는 정문에서 방까지 거리
    y=n%h # y는 몇 층을 입력받을지
    if y==0:
        y=h
        x-=1
    print(y*100+x)

    
        
    

            
            
        
    
    


            
    