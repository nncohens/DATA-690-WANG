
# coding: utf-8

# In[1]:


print ("Hello World")


# In[3]:


get_ipython().run_line_magic('run', 'hello_world.py')


# In[4]:


import numpy as np


# In[8]:


data = {i : np.random.randn() for i in range(7)}


# In[10]:


data


# In[12]:


from numpy.random import randn
data = {i : randn() for i in range(7)}
print(data)


# In[14]:


an_apple = 27
an_example = 42
an_apple and an_example any


# In[17]:


b = [1,2,3]
b.append 
b.count 
b.insert 
b.reverse 
b.clear 
b.extend 
b.pop 
b.sort 
b.copy 
b.index 
b.remove


# In[18]:


import datetime


# In[19]:


datetime.date


# In[23]:





# In[25]:


datasets/movielens/
datasets/movielens/movies.dat
datasets/movielens/README
datasets/movielens/ratings.dat
datasets/movielens/users.dat


# In[26]:


path = 'datasets/movielens/


# In[32]:


b = [1,2,3]


# In[33]:


get_ipython().run_line_magic('pinfo', 'b')


# In[29]:


get_ipython().run_line_magic('pinfo', 'print')


# In[31]:


get_ipython().run_line_magic('pinfo', 'b')


# In[35]:


#def add_numbers(a,b):
    return a+b


# In[36]:


get_ipython().run_line_magic('pinfo', 'add_numbers')
Signature: add_numbers(a,b)
Docstring:
Add two numbers together


# In[42]:


np.*load*? #Something here is incorrect. I am not sure what it is
np._loader_
np.load
np.loads


# In[40]:


def f(x,y,z):  
    return (x+y) /z
a = 5
b = 6
c = 7.5

result = f(a,b,c)


# In[41]:


get_ipython().run_line_magic('run', 'ipython_script_test.py')


# In[44]:


a = np.random.randn(100,100)
get_ipython().run_line_magic('timeit', 'np.dot(a,a)')
1000 loops, best of 3: 20.9 


# In[45]:


get_ipython().run_line_magic('matploblib', 'inline')


# In[46]:


import matplotlib.pyplot as plt
plt.plot(np.random.randn(50).cumsum())


# In[47]:


def append_element(some_list, element):
    some_list.append(element)

append_


# In[48]:


def append_element(some_list, element):
    some_list.append(element


# In[49]:


def append_element(some_list, element):
    some_list.append(element)


# In[50]:


data = [1,2,3]
append_element(data,4)


# In[51]:


data


# In[52]:


a = 5
type(a)


# In[53]:


a = "foo"
type(a)


# In[54]:


a = 4.5
b=2
print('a is {0}, b is {1}'.format(type(a), type(b)))


# In[55]:


a/b


# In[56]:


a = 5
isinstance(a, int)


# In[57]:


a = 5;b=4.5
isinstance(a, (int, float))
isinstance(b, (int, float))


# In[58]:


a = "foo"
getattr(a, 'split')


# In[59]:


5-7


# In[60]:


12+21.5


# In[61]:


5<= 2


# In[62]:


a = [1,2,3]
b=a
c=list(a)
a is b


# In[63]:


a is not c


# In[64]:


a = None
a is None


# In[68]:


a_list = ['foo', 2, [4,5]]
a_list[2] = (3,4) #will replace anything after 2 #mutable- can be modified
a_list


# In[69]:


ival = 17239871
ival **6


# In[70]:


fval = 7.243
fval2 = 6.78e-5


# In[71]:


3/2


# In[72]:


#//  drops the fraction (rounds down)
3//2


# In[76]:


a = "one way of writing a string"
b='another way of writing a string'
c= """
This is a longer string that 
spans multiple lines
"""


# In[77]:


c.count('\n') #counts the lines of text


# In[79]:


a = 5.6
s =str(a) #indicating s is a string
print(s)


# In[80]:


s = 'python'
list(s)


# In[81]:


s[:3] #first characters 0,1,2


# In[82]:


s = '12\\34'
print(s)


# In[83]:


s = r'this\has\no\special\characters' # r stands for raw
s


# In[85]:


#concatenating strings
a = 'this is the first half '
b = 'and this is the second half'
a+b


# In[93]:


template = '{0:.2f} {1:s} are worth US${2:d}'


# In[94]:


template.format(4.5560, 'Argentine Pesos',1)


# In[ ]:


# {0:.2f} format the 1st argument as floating point with 2 decimals 0-1st pos
#{1:s} format as string are worth US$                 1-2nd pos
#{2:d} format as an exact integer                     2-3rd pos


# In[95]:


from datetime import datetime, date, time #dont understand
dt =datetime(2011, 10,29,20,30,21)
dt.day


# In[96]:


dt.minute


# In[97]:


dt.date() #not clear


# In[101]:


if x<0:
    print("It's negative")
elif x == 0:
    print ('Equal to zero')
elif 0<x<5:
    print('Postive but smaller than 5')
else:
    print ('Positive and larger than or equal to 5')


# In[102]:


a = 5;b =7
c=8;d =4
if a<b or c>d:
    print('Made it')


# In[104]:


sequence = [1, 2, 0, 4, 6, 5, 2, 1]
total_until_5 = 0
for value in sequence:
 if value == 5:
     break
 total_until_5 += value


# In[112]:


:  for i in range(4):
:      for j in range(4):
:         if j > i:
:             break
:       print((i, j))
(0,0)
(1,0)
(1,1)
(2,0)
(2,1)
(2,2)
(3,0)
(3,1)
(3,2)
(3,3)


# In[113]:


x = 256
total = 0
while x > 0:
    if total > 500:
        break
    total += x
    x = x // 2

