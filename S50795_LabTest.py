#!/usr/bin/env python
# coding: utf-8

# In[120]:


def countSetBits(n):
    count = 0
    while (n):
        count += n & 1
        n >>=1
    return count

i = int(input('Enter a number: '))
print("number of bit with value 1 =", countSetBits(i))


# In[85]:


import collections

s = "an apple is not a tomato"
i = s.replace(" ", "")

print(collections.Counter(i).most_common(1)[0])


# In[42]:


i = "I have Python exam, he he he"

print("The text is: "+ i)

res = len(i.split())

print("The number of the words in the text: " ,res)


# In[125]:


def multiple_by_two(x):
    return x*2

def add_numbers(a, b):
    return a+b

def print_arguments(*args):
    print(f"arguments are:{args}")

augmented_multiple_by_two = print_arguments(multiple_by_two(10))
x = augmented_multiple_by_two

augmented_add_numbers = print_arguments(add_numbers(3, 4))
x = augmented_add_numbers


# In[133]:


def multiple_by_two(x):
    return x*2

def multiple_by_three(x):
    return x*3

def multiply_output(*args):
    print(f"arguments are:{args}")
    
augmented_multiple_by_three = multiply_output(multiple_by_two(multiple_by_three(10)))
x = augmented_multiple_by_three


# In[134]:


def multiple_by_two(x):
    return x*2

def add_numbers(a, b):
    return a+b

def augment_function(*args):
    print(f"arguments are:{args}")
    
decorated_function = augment_function(multiple_by_two(add_numbers(3, 4)))
x = decorated_function


# In[ ]:




