import random
n=random.randint(0,99)
g=0
while (g!=n):
    g=int(input("請輸入1-99內的常數:"))
    if g <=0:
        print("錯誤")
    elif g >=100:
        print("錯誤")
    elif g>n:
        print("小一點")
    elif g<n:
        print("大一點")
    else:
        print("bingo")
