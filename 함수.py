# 백준 알고리즘 15596

# for 함수로 푸는 방법
def solve(a):
    sum = 0
    for i in a:
        sum += i
    return sum

# sum 함수를 이용해 푸는 방법
def solve(a):
  return sum(a)

# 백준 알고리즘 4673

numbers = list(range(1, 10001))
remove_list = []  
for num in numbers :
    for n in str(num):
        num += int(n) 
    if num <= 10000:  
        remove_list.append(num)  

for remove_num in set(remove_list) : 
    numbers.remove(remove_num)
for self_num in numbers :  
    print(self_num)

# 백준 알고리즘 1065

def han(n):
    count = 0
    if (n < 100):
        return n
    else:
        for i in range(100,(n+1)):
            h = (i//100) # 100의 자리
            t = ((i%100) // 10) # 10의 자리
            o = ((i%100) % 10) # 1의 자리
            
            if ((h - t) == (t - o)):
                count += 1
        return (99 + count) # 1~99는 한수이므로 개수에 포함
x = int(input())
hancount = han(x)
print(hancount)