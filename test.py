def han(n):
    count = 0
    if (n < 100):
        return n
    else:
        for i in range(100,(n+1)):
            h = (i//100) 
            t = ((i%100) // 10) 
            o = ((i%100) % 10) 
            
            if ((h - t) == (t - o)):
                count += 1
        return (99 + count) 
x = int(input())
hancount = han(x)
print(hancount)


        


  



  