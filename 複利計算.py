m=int(input("請輸入本金:"))
r=float(input("請輸入年利率:"))
y=int(input("請輸入時間:"))
t=y+1
for i in range(1,t):
    g=m*(1+r)**i
    print("第%s年本利和為%d" % (i,g))#去小數
