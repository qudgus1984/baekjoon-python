# ���� �˰��� 15596

# for �Լ��� Ǫ�� ���
def solve(a):
    sum = 0
    for i in a:
        sum += i
    return sum

# sum �Լ��� �̿��� Ǫ�� ���
def solve(a):
  return sum(a)

# ���� �˰��� 4673

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

# ���� �˰��� 1065

def han(n):
    count = 0
    if (n < 100):
        return n
    else:
        for i in range(100,(n+1)):
            h = (i//100) # 100�� �ڸ�
            t = ((i%100) // 10) # 10�� �ڸ�
            o = ((i%100) % 10) # 1�� �ڸ�
            
            if ((h - t) == (t - o)):
                count += 1
        return (99 + count) # 1~99�� �Ѽ��̹Ƿ� ������ ����
x = int(input())
hancount = han(x)
print(hancount)