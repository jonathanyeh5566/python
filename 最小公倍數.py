
# coding: utf-8

# In[5]:


a = int(input("請輸入 a 的值"))
b = int(input("請輸入 b 的值"))
maxno=a*b
for i in range(1,maxno+1):
    if(i % a==0 and i*b==0):
        break
print(i)


# In[ ]:


6
4

