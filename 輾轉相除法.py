
# coding: utf-8

# In[19]:


a=int(input("請輸入正整數:"))
b=int(input("請輸入正整數:"))
if a<b:
    a,b=b,a
r = a%b
while r != 0:
    a = b
    b =r
    r = a%b
gcd = b
print(b)
    
    

