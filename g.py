m=int(input("請輸入本金:"))
r=float(input("請輸入年利率:"))
y=int(input("請輸入目標值:"))
b=0
g=0
while g<=y:
    b+=1
    g=m*(1+r)**b
print(b)
