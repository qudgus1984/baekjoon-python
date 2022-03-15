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

            
    