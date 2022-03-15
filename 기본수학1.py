# 백준 알고리즘 1712

A,B,C = map(int, (input().split())) # A는 고정비용, B는 가변비용, C는 노트북 가격
X = (A + (B * X))/C
if X == int(X):
    print(X)
else:
    print(-1)
