
# coding: utf-8

# In[28]:


a = int(input("請輸入 a 的值"))
c=0
print("因數:",end=" ")
if a<0:
    print("不是")
else:
    for i in range(1, a+1):
        if (a%i)==0:
            print(int(i),end=" ")
            c+=1
if c==2:
    print("是")
else:
    print("不是")
