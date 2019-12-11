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

for z in range(1,6):
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
        continue
print(c)
