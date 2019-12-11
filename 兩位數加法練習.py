c=0
while c<3 :
    import random
    a=random.randint(10,99)
    b=random.randint(10,99)
    q=a+b
    n=int(input("請輸入%d+%d=?"%(a,b)))

    if q==n:
        print("對")
        c=c+1
        continue
    else:
        print("錯")
        c=0
        continue
print("成功")




#
c=0
w=0
while w<5 :
    import random
    a=random.randint(10,99)
    b=random.randint(10,99)
    q=a+b
    n=int(input("請輸入%d+%d=?"%(a,b)))
    w+=1
    if q==n:
        print("對")
        c=c+1
        continue
    else:
        print("錯")
        continue
print(w)
