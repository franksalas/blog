---
title: Python Basics Cheet Sheet
date: 2018-06-09
tags: 
slug: python-basics-cheet-sheet
draft: true
toc: false
---


## Variables adn Data Types

### Variable Assignment


```python
x = 5
```


```python
x
```




5



## Calcuations With Variables


```python
x+2  # sum of two variables
```




7




```python
x-2  # substraction of two variables
```




3




```python
x*2  # multiplication of two variables
```




10




```python
x**2  # exponentional of a variable
```




25




```python
x%2  # remainder of a variable
```




1




```python
x/float(2)  # division of a variable
```




2.5



## Types and Type Conversion

### Varibles to string


```python
str('5')
```




'5'




```python
str('3.5')
```




'3.5'



### Variables to integers


```python
int(5)
```




5



### Variables to floats


```python
float(5)
```




5.0



## Variables to booleans


```python
bool(True)
```




True



## Asking for Help


```python
help(str)
```


## Strings


```python
my_string = 'thisStringIsAwesome'
my_string
```




'thisStringIsAwesome'



## String Operations


```python
 my_string * 2
```




'thisStringIsAwesomethisStringIsAwesome'




```python
 my_string + 'Innit'
```




    'thisStringIsAwesomeInnit'




```python
'm' in my_string
```




    True



## Lists


```python
a = 'is'
b = 'nice'
my_list = ['my', 'list', a, b]
my_list2 = [[4,5,6,7], [3,4,5,6]]
```

## Selecting List Elements

### Subset


```python
my_list[1]  # select item at index 1
```




    'list'




```python
my_list[-3]  # select 3rd last item
```




    'list'



### Slice


```python
my_list[1:3]  # Select itehms at index1 and 2
```




    ['list', 'is']




```python
my_list[1:]  # select items after index 0
```




    ['list', 'is', 'nice']




```python
my_list[:3]  # select items before index 3
```




    ['my', 'list', 'is']




```python
my_list[:]  # copy my_list
```




    ['my', 'list', 'is', 'nice']



### Subset Lists of Lists

```python
my_list[list][itemOfList]
```


```python
my_list2[1][0]
```




    3




```python
my_list2[1][:2]
```




    [3, 4]



## List Operations


```python
my_list + my_list
```




    ['my', 'list', 'is', 'nice', 'my', 'list', 'is', 'nice']




```python
my_list * 2
```




    ['my', 'list', 'is', 'nice', 'my', 'list', 'is', 'nice']



## List Methods


```python
my_list.index(a)  # get the index of an item
```




    2




```python
my_list.count(a)  # count an item
```




    1




```python
my_list.append('!')  #append an item at a time
```


```python
my_list.remove('!')  # remove an item
```


```python
del(my_list[0:1])    # remove an item
```


```python
my_list.reverse()    #reverse the list
```


```python
my_list.extend('!')  # append an item
```


```python
my_list.pop(-1)     # remove an item
```




    '!'




```python
my_list.insert(0,'!')  # insert an item
```


```python
my_list.sort()   # sort the list
```

## String Methods


```python
my_string.upper()  # string to uppercase
```




    'THISSTRINGISAWESOME'




```python
my_string.lower()  # string to lowercase
```




    'thisstringisawesome'




```python
my_string.count('w')  # count string elements
```




    1




```python
my_string.replace('e', 'i')  # replace string elements
```




    'thisStringIsAwisomi'




```python
my_string.strip()  # strip whitespaces
```




    'thisStringIsAwesome'



## Libraries


```python
import numpy as np   # import libraries
```


```python
from math import pi  # selective import
```

## NumPy Arrays


```python
my_list = [1, 2, 3, 4]
my_array = np.array(my_list)
my_2darray = np.array([[1,2,3],[4,5,6]])
other_array = np.array([99,98,97,96])
```

## Selecting Numpy Array Elements
Index starts at 0


```python
my_array[1]  # select item at index 1
```




    2




```python
my_array[0:2]  # select items at index 0 and 1
```




    array([1, 2])




```python
my_2darray[:,0]  # my_2darray[rows, columns]
```




    array([1, 4])



## NumPy Array Functions


```python
my_array.shape  # get the dimensions of the array
```




    (4,)




```python
np.insert(my_array, 1, 5)  # insert items in an array
```




    array([1, 5, 2, 3, 4])




```python
np.delete(my_array,[1])  # delete items in an array
```




    array([1, 3, 4])




```python
np.mean(my_array)  # mean of the array
```




    2.5




```python
np.median(my_array)  # median of the array
```




    2.5




```python
np.std(my_array)  # standar deviatoin
```




    1.118033988749895


