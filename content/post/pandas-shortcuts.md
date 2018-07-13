---
title: Pandas cheet sheet
date: 2016-01-09
draft: true
keywords: []
description: ""
tags: []
categories: []
slug: pandas-tux
comment: false
toc: false
autoCollapseToc: false
postMetaInFooter: false
hiddenFromHomePage: false
reward: false
mathjax: false
mathjaxEnableSingleDollar: false
mathjaxEnableAutoNumber: false
---
<!--more-->

## Load library


```python
import pandas as pd
```

```python
df = pd.DataFrame(
{"a" : [4 ,5, 6],
"b" : [7, 8, 9],
"c" : [10, 11, 12]},
index = [1, 2, 3])
```

```python
df
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
    .dataframe tbody tr th {
        vertical-align: top;
    }
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>7</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>8</td>
      <td>11</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6</td>
      <td>9</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>




```python
print(df)
```

       a  b   c
    1  4  7  10
    2  5  8  11
    3  6  9  12


## Series
A one dimensional laveled array


```python
s = pd.Series([3, -5, 7, 4],  index=['a',  'b',  'c',  'd'])
```

```python
print(s)
```

    a    3
    b   -5
    c    7
    d    4
    dtype: int64


## Dataframe
A two-dimensional labeled data structure with columns of potentially different types


```python
data = {'Country': ['Belgium',  'India',  'Brazil'],
         'Capital': ['Brussels',  'New Delhi',  'Brasilia'],
         'Population': [11190846, 1303171035, 207847528]}

df = pd.DataFrame(data,columns=['Country',  'Capital',  'Population'])
```

```python
print(df)
```

       Country    Capital  Population
    0  Belgium   Brussels    11190846
    1    India  New Delhi  1303171035
    2   Brazil   Brasilia   207847528



```python
df
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
    .dataframe tbody tr th {
        vertical-align: top;
    }
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Capital</th>
      <th>Population</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Belgium</td>
      <td>Brussels</td>
      <td>11190846</td>
    </tr>
    <tr>
      <th>1</th>
      <td>India</td>
      <td>New Delhi</td>
      <td>1303171035</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Brazil</td>
      <td>Brasilia</td>
      <td>207847528</td>
    </tr>
  </tbody>
</table>
</div>


